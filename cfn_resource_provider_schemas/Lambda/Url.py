SCHEMA = {
  "typeName" : "AWS::Lambda::Url",
  "description" : "Resource Type definition for AWS::Lambda::Url",
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : False
  },
  "properties" : {
    "TargetFunctionArn" : {
      "description" : "The Amazon Resource Name (ARN) of the function associated with the Function URL.",
      "type" : "string",
      "pattern" : "^(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\\d{1}:)?(\\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:((?!\\d+)[0-9a-zA-Z-_]+))?$"
    },
    "Qualifier" : {
      "description" : "The alias qualifier for the target function. If TargetFunctionArn is unqualified then Qualifier must be passed.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 128,
      "pattern" : "((?!^[0-9]+$)([a-zA-Z0-9-_]+))"
    },
    "AuthType" : {
      "description" : "Can be either AWS_IAM if the requests are authorized via IAM, or NONE if no authorization is configured on the Function URL.",
      "type" : "string",
      "enum" : [ "AWS_IAM", "NONE" ]
    },
    "InvokeMode" : {
      "description" : "The invocation mode for the function's URL. Set to BUFFERED if you want to buffer responses before returning them to the client. Set to RESPONSE_STREAM if you want to stream responses, allowing faster time to first byte and larger response payload sizes. If not set, defaults to BUFFERED.",
      "type" : "string",
      "enum" : [ "BUFFERED", "RESPONSE_STREAM" ]
    },
    "FunctionArn" : {
      "description" : "The full Amazon Resource Name (ARN) of the function associated with the Function URL.",
      "type" : "string",
      "pattern" : "^(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\\d{1}:)?(\\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:((?!\\d+)[0-9a-zA-Z-_]+))?$"
    },
    "FunctionUrl" : {
      "description" : "The generated url for this resource.",
      "type" : "string"
    },
    "Cors" : {
      "$ref" : "#/definitions/Cors"
    }
  },
  "definitions" : {
    "AllowHeaders" : {
      "items" : {
        "type" : "string",
        "minLength" : 1,
        "maxLength" : 1024
      },
      "type" : "array",
      "minItems" : 1,
      "maxItems" : 100,
      "insertionOrder" : True
    },
    "AllowMethods" : {
      "items" : {
        "type" : "string",
        "enum" : [ "GET", "PUT", "HEAD", "POST", "PATCH", "DELETE", "*" ]
      },
      "type" : "array",
      "minItems" : 1,
      "maxItems" : 6,
      "insertionOrder" : True
    },
    "AllowOrigins" : {
      "items" : {
        "type" : "string",
        "minLength" : 1,
        "maxLength" : 253
      },
      "type" : "array",
      "minItems" : 1,
      "maxItems" : 100,
      "insertionOrder" : True
    },
    "ExposeHeaders" : {
      "items" : {
        "type" : "string",
        "minLength" : 1,
        "maxLength" : 1024
      },
      "type" : "array",
      "minItems" : 1,
      "maxItems" : 100,
      "insertionOrder" : True
    },
    "Cors" : {
      "additionalProperties" : False,
      "properties" : {
        "AllowCredentials" : {
          "description" : "Specifies whether credentials are included in the CORS request.",
          "type" : "boolean"
        },
        "AllowHeaders" : {
          "description" : "Represents a collection of allowed headers.",
          "$ref" : "#/definitions/AllowHeaders"
        },
        "AllowMethods" : {
          "description" : "Represents a collection of allowed HTTP methods.",
          "$ref" : "#/definitions/AllowMethods"
        },
        "AllowOrigins" : {
          "description" : "Represents a collection of allowed origins.",
          "$ref" : "#/definitions/AllowOrigins"
        },
        "ExposeHeaders" : {
          "description" : "Represents a collection of exposed headers.",
          "$ref" : "#/definitions/ExposeHeaders"
        },
        "MaxAge" : {
          "type" : "integer",
          "minimum" : 0,
          "maximum" : 86400
        }
      },
      "type" : "object"
    }
  },
  "required" : [ "TargetFunctionArn", "AuthType" ],
  "createOnlyProperties" : [ "/properties/TargetFunctionArn", "/properties/Qualifier" ],
  "readOnlyProperties" : [ "/properties/FunctionUrl", "/properties/FunctionArn" ],
  "primaryIdentifier" : [ "/properties/FunctionArn" ],
  "propertyTransform" : {
    "/properties/TargetFunctionArn" : "$lookup($match(TargetFunctionArn,/(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}(-gov)?-[a-z]+-[0-9]{1}:)?([0-9]{12}:)?(function:)?([a-zA-Z0-9-_]+)(:((?![0-9]+)[0-9a-zA-Z-_]+))?/)['groups'], 'groups')[6]"
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "lambda:CreateFunctionUrlConfig" ]
    },
    "read" : {
      "permissions" : [ "lambda:GetFunctionUrlConfig" ]
    },
    "update" : {
      "permissions" : [ "lambda:UpdateFunctionUrlConfig" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "TargetFunctionArn" : {
            "description" : "The Amazon Resource Name (ARN) of the function associated with the Function URL.",
            "type" : "string",
            "pattern" : "^(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\\d{1}:)?(\\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:((?!\\d+)[0-9a-zA-Z-_]+))?$"
          }
        },
        "required" : [ "TargetFunctionArn" ]
      },
      "permissions" : [ "lambda:ListFunctionUrlConfigs" ]
    },
    "delete" : {
      "permissions" : [ "lambda:DeleteFunctionUrlConfig" ]
    }
  }
}