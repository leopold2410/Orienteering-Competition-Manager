#!/bin/bash

cd backend/api-gateway
pip install masonite-cli
craft install
python -m pytest