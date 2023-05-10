# path:  .github/workflows/saucelabs.yml

on: workflow_dispatch
# on: 
#   push:
#     branches: [ "main" ]

env:
  SAUCE_USERNAME: ${{secrets.SAUCE_USERNAME}}
  SAUCE_ACCESS_KEY: ${{secrets.SAUCE_ACCESS_KEY}}
  SAUCE_URL: ${{secrets.SAUCE_URL}}

jobs:
  main:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install selenium
      - name: Test
        run: |
          python3 -m unittest cloud_test.py
