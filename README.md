# tap-hubspot

`tap-hubspot` is a Singer tap for hubspot.

Build with the [Singer SDK](https://gitlab.com/meltano/singer-sdk).

# CONTRIBUTIONS ONLY

**What does this mean?** The only way fixes or new features will be added is by people submitting PRs.

## Installation

- [ ] `Install from your git repo:`

```bash
pip install -e git+ssh://git@github.com:tucows/tap-hubspot.git#egg=tap-hubspot
```

## Configuration

### Accepted Config Options

- [ ] `Configuration parameters:` Stored in a json file and provided with the mandatory --config option
```bash
{
    "api_url": "https://api.hubapi.com",
    "hapikey": "********-****-****-****-**********"
}
```

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-hubspot --about
```

## Usage
`After installation:` Streams output to standard output when you run
```bash
tap-hubspot --config sample_tap_hubspot_config.json
```

### Generating schemas using singer-infer-schema from singer-tools package
`Generate schemas for objects:` Update the stream:endpoint dictionary in schema.py then 
```bash
python schema.py --config sample_tap_hubspot_config.json
```

You can easily run `tap-hubspot` by itself or in a pipeline using [Meltano](www.meltano.com).

### Executing the Tap Directly

```bash
tap-hubspot --version
tap-hubspot --help
tap-hubspot --config sample_tap_hubspot_config.json --discover > ./catalog.json
```

## Developer Resources

- [ ] `Developer TODO:` As a first step, scan the entire project for the text "`TODO:`" and complete any recommended steps, deleting the "TODO" references once completed.

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tap_hubspot/tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-hubspot` CLI interface directly using `poetry run`:

```bash
poetry run tap-hubspot --help
```

### Testing with [Meltano](meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any _"TODO"_ items listed in
the file.

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-hubspot
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-hubspot --version
# OR run a test `elt` pipeline:
meltano etl tap-hubspot target-jsonl
```

### Singer SDK Dev Guide

See the [dev guide](../../docs/dev_guide.md) for more instructions on how to use the Singer SDK to 
develop your own taps and targets.
