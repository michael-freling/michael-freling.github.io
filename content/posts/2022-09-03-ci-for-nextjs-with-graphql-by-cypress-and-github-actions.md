---
title: "CI for Next.js with GraphQL by Cypress and GitHub Actions"
date: 2022-09-03T14:29:20-07:00
draft: false
---

CI is used to run automated testings before merging a change into the main branch.
For Node.js application, I set up GitHub Action to run

- Cypress component testings for frontend testings
  - Mock the response of GraphQL
- Jest testings for GraphQL resolvers
  - Use a docker compose for a MySQL and a Firebase emulator on local and GitHub Action environments
- Unit testings for firebase storage rules

But I couldn't figure out these things

- How to implement Google Sign In of Firebase for Cypress component testings
  - I used `signInWithRedirect` and `getRedirectResult` of `firebase/auth`
  - Couldn't click any UI components even I used `cy.origin` nor `chromeWebSecurity: false`

Usually, granular unit tesitngs are helpful to increase the reusability of
But I chose to test only integration testings of a page level or a resolver level to make sure behaviors only.

---

# Testings

## Cypress

How to set up is described in [the Next.js official document](https://nextjs.org/docs/testing#manual-setup).

Because I wanted to mock some behaviors and reuse functions defined on production code, I used component testings instead of e2e testings.
Besides, I couldn't figure out how to sign in by Google before implementing a test case.

Compare to use jest for a browser testings, cypress component testings are useful not to install and set up many of modules for jest, and easier to emulator DOM events.

There are a few things that I need to look into when I implemented component testings.

- Cypress doesn't support [multiple tabs](https:// docs.cypress.io/guides/references/trade-offs#Multiple-tabs).
- For handling the URL parameters of a next.js, there is a [react router](https://docs.cypress.io/guides/component-testing/custom-mount-react#React-Router).

## Testings GraphQL resolvers with TypeGraphQL by Jest

How to set up jest for Next.js application is described in [the Next.js official document](https://nextjs.org/docs/testing#jest-and-react-testing-library).
But I just used it for server side testings, so I didn't install `@testing-library/react` nor `@testing-library/jest-dom`.

To use TypeGraphQL, it requires to set up a few things

### For TypeScript configurations

First, install a few packages

```shell
npm install --save-dev @types/jest ts-jest ts-node
```

Then update jest.config.ts to next. Note that `preset` will be updated later.

```diff
+ import { pathsToModuleNameMapper } from "ts-jest";
+ const { compilerOptions } = require("./tsconfig");

const customJestConfig = {
  // Add more setup options before each test is run
  // setupFilesAfterEnv: ["<rootDir>/jest.setup.js"],
  // if using TypeScript with a baseUrl set to the root directory then you need the below for alias' to work
+  preset: "ts-jest",
+  moduleNameMapper: pathsToModuleNameMapper(compilerOptions.paths),
  moduleDirectories: ["node_modules", "<rootDir>/"],
  //  testEnvironment: "jest-environment-jsdom",
};
```

#### Enable to use async and await on jest files

Just following [this document](https://github.com/kulshekhar/ts-jest/issues/2057#issuecomment-1031111683).

At first, use `--experimental-vm-modules` option on node to start a jest.

```diff
- jest --watch
+ node --no-warnings --experimental-vm-modules node_modules/jest/bin/jest.js --watch
```

Then use `default-esm` preset in `jest.config.ts`.

```diff
-  "preset": "ts-jest",
+  "preset": "ts-jest/presets/default-esm",
```

### For TypeGraphQL

For `type-graphql`, import reflect-metadata has to be imported before running test cases.
Add a line to import it on `jest.setup.ts` loaded on `setupFilesAfterEnv`.

### Error: jest is not defined

An error `jest is not defined` occured when I tried to use `jest.setTimeout` function.

Add `import { jest } from "@jest/global";` to solve this, which is discussed in [this comment](https://github.com/facebook/jest/issues/9430#issuecomment-616232029).

### Get a file path for a fixture file

To get a fixture file from the relative path of the test file, use `path.resolve` and `url.fileURLToPath`

```ts
import path from "path";
import { fileURLToPath } from "url";

path.resolve(
  path.dirname(fileURLToPath(import.meta.url)),
  "../../fixtures/video.mp4"
);
```

### For firebase of jest

If `firebase-admin/auth` is used, there was an error like next.
To avoid this error, use `getAuth` from a `firebase-admin/auth` package.

```shell
    SyntaxError: The requested module 'firebase-admin' does not provide an export named 'auth'

      at async Runtime.linkAndEvaluateModule (node_modules/jest-runtime/build/index.js:828:5)
```

Also, in order to connect to firebase auth and storage emulators from jest testings, define following environment variables.
This is also from [this github issue](https://github.com/firebase/firebase-admin-node/issues/776#issuecomment-1200036590).

- `FIREBASE_AUTH_EMULATOR_HOST`
- `FIREBASE_STORAGE_EMULATOR_HOST`

### Suggest jest functions by VSCode with Cypress

Suggest jet functions of test files didn't work correctly with Cypress.
It's because chai functions are installed by Cypress and they are suggested.
And this was not a bug but a configuration issue, and other person also reported in the [GitHub issue](https://github.com/cypress-io/cypress/issues/6156).

For my case, I put every jest test cases into `__tests__` directory, so define `tsconfig.json` in the directory and define `typeAcquisition` to include `jest`

```json
{
  "extends": "../tsconfig.json",
  "typeAcquisition": {
    "include": ["jest"]
  },
  "include": ["**/*.ts"]
}
```

---

# Containers for MySQL and Firebase emulators

## Run a MySQL as a container

Use Docker Compose to build a MySQL container.
In order to initialize a schema for this application, `prisma` is used to manage initiailze schemas.
To access a different MySQL container when jest runs, prepare a different env file and mount it to `.env` file on prisma container.

## Run a Firebase emulator as a container

Build an image for a firebase emulator as a container.
I set up by simple Dockerfile like next.

```dockerfile
FROM node:18.2

EXPOSE 4000
EXPOSE 9099
EXPOSE 9199

RUN npm install -g firebase-tools

RUN apt update && apt install -y default-jre

ENTRYPOINT [ "firebase" ]
```

And in order to access the container from the host, add `host: 0.0.0.0` to `firebase.json` by following a few comments like [this](https://github.com/firebase/firebase-tools-ui/issues/464#issuecomment-782913719) or [this](https://github.com/firebase/firebase-tools/issues/3121#issue-805381619).

```diff
{
  "storage": {
    "rules": "storage.rules"
  },
  "emulators": {
    "auth": {
      "port": 9099,
+      "host": "0.0.0.0"
    },
    "storage": {
      "port": 9199,
+      "host": "0.0.0.0"
    },
    "ui": {
      "enabled": true,
+      "host": "0.0.0.0"
    }
  }
}
```

---

# GitHub Actions

## Cypress component testings

Follow [this setup](https://github.com/cypress-io/github-action#component-tests) on GitHub Actions to run cypress component testings.

## Docker layer caches of GitHub Actions

There is an [article](https://evilmartians.com/chronicles/build-images-on-github-actions-with-docker-layer-caching) to cache docker images by a Dockerfile.
But in order to cache docker layer images for a docker compose, it's required to use a different way.
And there is [another GitHub Action](https://github.com/satackey/action-docker-layer-caching) to do so.
I just used it to cache them.

## Errors during eslint

Functions naming `useXXX` even on a server side is recognized as a React hook and made an error.

```shell
334:5  Error: React Hook "useGenericAuth" cannot be called at the top level. React Hooks must be called in a React function component or a custom React Hook function.  react-hooks/rules-of-hooks
```

I couldn't find a good way to exclude these react hooks only for specific directories like code of server sides, so I just added next line of the function using the function to disable the rule temporarily.

```ts
// eslint-disable-next-line react-hooks/rules-of-hooks
```
