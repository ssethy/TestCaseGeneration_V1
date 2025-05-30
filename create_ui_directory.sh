#!/bin/bash

mkdir -p test-case-generator-ui/{public/assets,src/{components,pages,services,context,store,router,utils,tests},k8s}

# Create placeholder files
touch test-case-generator-ui/public/assets/logo.png
touch test-case-generator-ui/src/components/{FileUploader.jsx,RequirementList.jsx,RequirementDetail.jsx,TestCaseTable.jsx,VersionSelector.jsx,DiffViewer.jsx}
touch test-case-generator-ui/src/pages/{RequirementUploadPage.jsx,RequirementsPage.jsx,RequirementTestCasesPage.jsx,CompareVersionsPage.jsx,NotFoundPage.jsx}
touch test-case-generator-ui/src/services/{requirementService.js,testCaseService.js}
touch test-case-generator-ui/src/context/AppContextProvider.jsx
touch test-case-generator-ui/src/store/useAppStore.js
touch test-case-generator-ui/src/router/index.jsx
touch test-case-generator-ui/src/utils/helpers.js
touch test-case-generator-ui/src/tests/{FileUploader.test.jsx,RequirementsPage.test.jsx,RequirementTestCasesPage.test.jsx,CompareVersionsPage.test.jsx}
touch test-case-generator-ui/src/{App.jsx,main.jsx}
touch test-case-generator-ui/{Dockerfile,tailwind.config.js,postcss.config.js,vite.config.js,package.json,.dockerignore,README.md}
touch test-case-generator-ui/k8s/{deployment.yaml,service.yaml,configmap.yaml}

