SCHEMA = {
  "typeName" : "AWS::Lambda::Version",
  "description" : "Resource Type definition for AWS::Lambda::Version",
  "additionalProperties" : False,
  "properties" : {
    "FunctionArn" : {
      "type" : "string",
      "description" : "The ARN of the version.",
      "pattern" : "^(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\\d{1}:)?(\\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\\$LATEST|[a-zA-Z0-9-_]+))?$"
    },
    "Version" : {
      "type" : "string",
      "description" : "The version number."
    },
    "CodeSha256" : {
      "type" : "string",
      "description" : "Only publish a version if the hash value matches the value that's specified. Use this option to avoid publishing a version if the function code has changed since you last updated it. Updates are not supported for this property."
    },
    "Description" : {
      "type" : "string",
      "description" : "A description for the version to override the description in the function configuration. Updates are not supported for this property.",
      "minLength" : 0,
      "maxLength" : 256
    },
    "FunctionName" : {
      "type" : "string",
      "description" : "The name of the Lambda function.",
      "minLength" : 1,
      "maxLength" : 140,
      "pattern" : "^(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\\d{1}:)?(\\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\\$LATEST|[a-zA-Z0-9-_]+))?$"
    },
    "ProvisionedConcurrencyConfig" : {
      "description" : "Specifies a provisioned concurrency configuration for a function's version. Updates are not supported for this property.",
      "$ref" : "#/definitions/ProvisionedConcurrencyConfiguration"
    },
    "RuntimePolicy" : {
      "description" : "Specifies the runtime management configuration of a function. Displays runtimeVersionArn only for Manual.",
      "$ref" : "#/definitions/RuntimePolicy"
    }
  },
  "definitions" : {
    "ProvisionedConcurrencyConfiguration" : {
      "type" : "object",
      "description" : "A provisioned concurrency configuration for a function's version.",
      "additionalProperties" : False,
      "properties" : {
        "ProvisionedConcurrentExecutions" : {
          "type" : "integer",
          "description" : "The amount of provisioned concurrency to allocate for the version."
        }
      },
      "required" : [ "ProvisionedConcurrentExecutions" ]
    },
    "RuntimePolicy" : {
      "type" : "object",
      "description" : "Runtime Management Config of a function.",
      "additionalProperties" : False,
      "properties" : {
        "RuntimeVersionArn" : {
          "type" : "string",
          "description" : "The ARN of the runtime the function is configured to use. If the runtime update mode is manual, the ARN is returned, otherwise None is returned.",
          "minLength" : 26,
          "maxLength" : 2048,
          "pattern" : "^arn:(aws[a-zA-Z-]*):lambda:[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\\d{1}::runtime:.+$"
        },
        "UpdateRuntimeOn" : {
          "type" : "string",
          "description" : "The runtime update mode."
        }
      },
      "required" : [ "UpdateRuntimeOn" ]
    }
  },
  "required" : [ "FunctionName" ],
  "readOnlyProperties" : [ "/properties/Version", "/properties/FunctionArn" ],
  "createOnlyProperties" : [ "/properties/FunctionName", "/properties/Description", "/properties/CodeSha256", "/properties/ProvisionedConcurrencyConfig", "/properties/RuntimePolicy" ],
  "primaryIdentifier" : [ "/properties/FunctionArn" ],
  "propertyTransform" : {
    "/properties/FunctionName" : "$split(FunctionName, \":\")[-1] $OR FunctionName"
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "lambda:PublishVersion", "lambda:GetFunctionConfiguration", "lambda:PutProvisionedConcurrencyConfig", "lambda:GetProvisionedConcurrencyConfig", "lambda:PutRuntimeManagementConfig", "lambda:GetRuntimeManagementConfig" ],
      "timeoutInMinutes" : 180
    },
    "read" : {
      "permissions" : [ "lambda:GetFunctionConfiguration", "lambda:GetProvisionedConcurrencyConfig", "lambda:GetRuntimeManagementConfig" ]
    },
    "delete" : {
      "permissions" : [ "lambda:GetFunctionConfiguration", "lambda:DeleteFunction" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "FunctionName" : {
            "description" : "The name of the Lambda function, version, or alias.",
            "type" : "string",
            "pattern" : "^(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\\d{1}:)?(\\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\\$LATEST|[a-zA-Z0-9-_]+))?$",
            "minLength" : 1,
            "maxLength" : 140
          }
        },
        "required" : [ "FunctionName" ]
      },
      "permissions" : [ "lambda:ListVersionsByFunction" ]
    }
  }
}