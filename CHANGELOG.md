# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## v2.2.1 (2024-02-06)

### Fix

- **deps**: update starlette requirement (#72)

## v2.2.0 (2023-11-06)

### Feat

- **deps**: update starlette requirement from ^0.31.0 to >=0.31,<0.33 (#65)

## v2.1.0 (2023-09-08)

### Feat

- **deps**: update apispec requirement from >=1,<6 to >=1,<7 (#64)

## v2.0.0 (2023-08-22)

### BREAKING CHANGE

- `py3.6` and `py3.7` have been dropped, please upgrade to `>=py3.8`

### Fix

- update bump action
- drop support for python deprecated versions and update packages

## v1.0.5 (2021-12-20)

### Fix

- **deps**: update apispec requirement from >=1,<5 to >=1,<6

## v1.0.4 (2021-07-15)

### Fix

- format to bump version

## [1.0.3] - 2019-11-12

- Bumped dependecies: starlette-apispec and dev deps

## [1.0.2] - 2019-06-12

### Fix

- `app.schema` was deprecated in starlette so the tests were fixed.

## [1.0.1] - 2019-02-16

- Restructured text syntax errors in README preventing a good render in pypi.

## [1.0.0] - 2019-02-16

- Support for apispec `^1.0.0`

## [1.0.0b1] - 2019-01-03

### BREAKING CHANGE

- Support for apispec `>1.0.0b5`

## [0.1.3] - 2018-12-18

- Improved version range from caret req to higher than `0.8.8`

## [0.1.2] - 2018-11-23

### Updated

- Documentation

## [0.1.1] - 2018-11-23

### Added

- Documentation
- APISpecSchemaGenerator ready to be used with starlette
