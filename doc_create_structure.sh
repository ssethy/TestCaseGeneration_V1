#!/bin/bash

# Define root folder
ROOT="document-preprocessor"

# Create directories
mkdir -p $ROOT/app/service/parsers
mkdir -p $ROOT/app/models
mkdir -p $ROOT/app/utils
mkdir -p $ROOT/tests
mkdir -p $ROOT/k8s

# Create placeholder files
touch $ROOT/app/main.py
touch $ROOT/app/routes.py
touch $ROOT/app/service/processor.py
touch $ROOT/app/service/parsers/docx_parser.py
touch $ROOT/app/service/parsers/pdf_parser.py
touch $ROOT/app/service/parsers/image_parser.py
touch $ROOT/app/models/request.py
touch $ROOT/app/models/response.py
touch $ROOT/app/utils/text_segmenter.py
touch $ROOT/tests/test_processor.py
touch $ROOT/tests/test_routes.py
touch $ROOT/Dockerfile
touch $ROOT/k8s/deployment.yaml
touch $ROOT/requirements.txt
touch $ROOT/README.md

touch document-preprocessor/app/__init__.py
touch document-preprocessor/app/service/__init__.py
touch document-preprocessor/app/service/parsers/__init__.py
touch document-preprocessor/app/models/__init__.py
touch document-preprocessor/app/utils/__init__.py
touch document-preprocessor/tests/__init__.py

# Create parser modules
touch $ROOT/app/service/parsers/docx_parser.py
touch $ROOT/app/service/parsers/pdf_parser.py
touch $ROOT/app/service/parsers/image_parser.py

# Create text segmentation logic
touch $ROOT/app/utils/text_segmenter.py



echo "✅ Document Preprocessor directory structure created successfully."

