# Python importable [AWS CFN resource provider schemas](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-type-schemas.html)

Downloaded from [AWS](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-type-schemas.html) and converted to python package.

Useful for schema validation using e.g. [jsonschema](https://pypi.org/project/jsonschema/).

## Usage example

```python
from cfn_resource_provider_schemas.Ecs import Taskdefinition
from jsonschema import Draft202012Validator

task_definition = {
    "ContainerDefinitions": [
        {
            "Cpu": "256",
            "Memory": "512",
        }
    ]
}

for error in sorted(validator.iter_errors(task_definition), key=str):
    _errors.append(f"{' > '.join(error.absolute_schema_path)}: {error.message}")
if _errors:
    raise ValueError("\n".join(_errors))
```
