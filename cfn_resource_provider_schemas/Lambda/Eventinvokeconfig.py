SCHEMA = {
  "typeName" : "AWS::Lambda::EventInvokeConfig",
  "description" : "The AWS::Lambda::EventInvokeConfig resource configures options for asynchronous invocation on a version or an alias.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "DestinationConfig" : {
      "description" : "A destination for events after they have been sent to a function for processing.",
      "type" : "object",
      "properties" : {
        "OnFailure" : {
          "$ref" : "#/definitions/OnFailure"
        },
        "OnSuccess" : {
          "$ref" : "#/definitions/OnSuccess"
        }
      },
      "additionalProperties" : False
    },
    "OnFailure" : {
      "description" : "The destination configuration for failed invocations.",
      "type" : "object",
      "properties" : {
        "Destination" : {
          "description" : "The Amazon Resource Name (ARN) of the destination resource.",
          "type" : "string",
          "pattern" : "^$|arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\\-])+:([a-z]{2}(-gov)?(-iso([a-z])?)?-[a-z]+-\\d{1})?:(\\d{12})?:(.*)",
          "minLength" : 0,
          "maxLength" : 350
        }
      },
      "required" : [ "Destination" ],
      "additionalProperties" : False
    },
    "OnSuccess" : {
      "description" : "The destination configuration for successful invocations.",
      "type" : "object",
      "properties" : {
        "Destination" : {
          "description" : "The Amazon Resource Name (ARN) of the destination resource.",
          "type" : "string",
          "pattern" : "^$|arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\\-])+:([a-z]{2}(-gov)?(-iso([a-z])?)?-[a-z]+-\\d{1})?:(\\d{12})?:(.*)",
          "minLength" : 0,
          "maxLength" : 350
        }
      },
      "required" : [ "Destination" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "DestinationConfig" : {
      "$ref" : "#/definitions/DestinationConfig"
    },
    "FunctionName" : {
      "description" : "The name of the Lambda function.",
      "type" : "string",
      "pattern" : "^(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}(-gov)?(-iso([a-z])?)?-[a-z]+-\\d{1}:)?(\\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\\$LATEST|[a-zA-Z0-9-_]+))?$"
    },
    "MaximumEventAgeInSeconds" : {
      "description" : "The maximum age of a request that Lambda sends to a function for processing.",
      "type" : "integer",
      "minimum" : 60,
      "maximum" : 21600
    },
    "MaximumRetryAttempts" : {
      "description" : "The maximum number of times to retry when the function returns an error.",
      "type" : "integer",
      "minimum" : 0,
      "maximum" : 2
    },
    "Qualifier" : {
      "description" : "The identifier of a version or alias.",
      "type" : "string",
      "pattern" : "^(|[a-zA-Z0-9$_-]{1,129})$"
    }
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "additionalProperties" : False,
  "required" : [ "FunctionName", "Qualifier" ],
  "primaryIdentifier" : [ "/properties/FunctionName", "/properties/Qualifier" ],
  "createOnlyProperties" : [ "/properties/FunctionName", "/properties/Qualifier" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "lambda:PutFunctionEventInvokeConfig" ]
    },
    "read" : {
      "permissions" : [ "lambda:GetFunctionEventInvokeConfig" ]
    },
    "update" : {
      "permissions" : [ "lambda:UpdateFunctionEventInvokeConfig" ]
    },
    "delete" : {
      "permissions" : [ "lambda:DeleteFunctionEventInvokeConfig" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "FunctionName" : {
            "$ref" : "resource-schema.json#/properties/FunctionName"
          }
        },
        "required" : [ "FunctionName" ]
      },
      "permissions" : [ "lambda:ListFunctionEventInvokeConfigs" ]
    }
  }
}