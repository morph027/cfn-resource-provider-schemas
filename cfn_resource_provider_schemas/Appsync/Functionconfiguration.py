SCHEMA = {
  "typeName" : "AWS::AppSync::FunctionConfiguration",
  "description" : "An example resource schema demonstrating some basic constructs and validation rules.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "AppSyncRuntime" : {
      "description" : "Describes a runtime used by an AWS AppSync pipeline resolver or AWS AppSync function. Specifies the name and version of the runtime to use. Note that if a runtime is specified, code must also be specified.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Name" : {
          "type" : "string",
          "description" : "The name of the runtime to use. Currently, the only allowed value is APPSYNC_JS."
        },
        "RuntimeVersion" : {
          "type" : "string",
          "description" : "The version of the runtime to use. Currently, the only allowed version is 1.0.0."
        }
      },
      "required" : [ "Name", "RuntimeVersion" ]
    },
    "SyncConfig" : {
      "description" : "Describes a Sync configuration for a resolver. Specifies which Conflict Detection strategy and Resolution strategy to use when the resolver is invoked.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ConflictDetection" : {
          "type" : "string",
          "description" : "The Conflict Detection strategy to use."
        },
        "ConflictHandler" : {
          "type" : "string",
          "description" : "The Conflict Resolution strategy to perform in the event of a conflict."
        },
        "LambdaConflictHandlerConfig" : {
          "$ref" : "#/definitions/LambdaConflictHandlerConfig"
        }
      },
      "required" : [ "ConflictDetection" ]
    },
    "LambdaConflictHandlerConfig" : {
      "type" : "object",
      "description" : "The LambdaConflictHandlerConfig when configuring LAMBDA as the Conflict Handler.",
      "additionalProperties" : False,
      "properties" : {
        "LambdaConflictHandlerArn" : {
          "type" : "string",
          "description" : "The Amazon Resource Name (ARN) for the Lambda function to use as the Conflict Handler."
        }
      }
    }
  },
  "properties" : {
    "FunctionId" : {
      "description" : "The unique identifier for the function generated by the service",
      "type" : "string"
    },
    "FunctionArn" : {
      "description" : "The ARN for the function generated by the service",
      "type" : "string"
    },
    "ApiId" : {
      "description" : "The AWS AppSync GraphQL API that you want to attach using this function.",
      "type" : "string"
    },
    "Code" : {
      "description" : "The resolver code that contains the request and response functions. When code is used, the runtime is required. The runtime value must be APPSYNC_JS.",
      "type" : "string"
    },
    "CodeS3Location" : {
      "description" : "The Amazon S3 endpoint (where the code is located??).",
      "type" : "string"
    },
    "DataSourceName" : {
      "description" : "The name of data source this function will attach.",
      "type" : "string"
    },
    "Description" : {
      "description" : "The function description.",
      "type" : "string"
    },
    "FunctionVersion" : {
      "description" : "The version of the request mapping template. Currently, only the 2018-05-29 version of the template is supported.",
      "type" : "string"
    },
    "MaxBatchSize" : {
      "description" : "The maximum number of resolver request inputs that will be sent to a single AWS Lambda function in a BatchInvoke operation.",
      "type" : "integer"
    },
    "Name" : {
      "description" : "The name of the function.",
      "type" : "string"
    },
    "RequestMappingTemplate" : {
      "description" : "The Function request mapping template. Functions support only the 2018-05-29 version of the request mapping template.",
      "type" : "string"
    },
    "RequestMappingTemplateS3Location" : {
      "description" : "Describes a Sync configuration for a resolver. Contains information on which Conflict Detection, as well as Resolution strategy, should be performed when the resolver is invoked.",
      "type" : "string"
    },
    "ResponseMappingTemplate" : {
      "description" : "The Function response mapping template.",
      "type" : "string"
    },
    "ResponseMappingTemplateS3Location" : {
      "description" : "The location of a response mapping template in an Amazon S3 bucket. Use this if you want to provision with a template file in Amazon S3 rather than embedding it in your CloudFormation template.",
      "type" : "string"
    },
    "Runtime" : {
      "description" : "Describes a runtime used by an AWS AppSync pipeline resolver or AWS AppSync function. Specifies the name and version of the runtime to use. Note that if a runtime is specified, code must also be specified.",
      "$ref" : "#/definitions/AppSyncRuntime"
    },
    "SyncConfig" : {
      "description" : "Describes a Sync configuration for a resolver. Specifies which Conflict Detection strategy and Resolution strategy to use when the resolver is invoked.",
      "$ref" : "#/definitions/SyncConfig"
    }
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "additionalProperties" : False,
  "required" : [ "ApiId", "DataSourceName", "Name" ],
  "readOnlyProperties" : [ "/properties/FunctionArn", "/properties/FunctionId" ],
  "writeOnlyProperties" : [ "/properties/CodeS3Location", "/properties/ResponseMappingTemplateS3Location", "/properties/RequestMappingTemplateS3Location" ],
  "createOnlyProperties" : [ "/properties/ApiId" ],
  "primaryIdentifier" : [ "/properties/FunctionArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "s3:GetObject", "appsync:CreateFunction" ]
    },
    "read" : {
      "permissions" : [ "appsync:GetFunction" ]
    },
    "update" : {
      "permissions" : [ "s3:GetObject", "appsync:UpdateFunction" ]
    },
    "delete" : {
      "permissions" : [ "appsync:DeleteFunction" ]
    },
    "list" : {
      "permissions" : [ "appsync:ListFunctions" ],
      "handlerSchema" : {
        "properties" : {
          "ApiId" : {
            "$ref" : "resource-schema.json#/properties/ApiId"
          }
        },
        "required" : [ "ApiId" ]
      }
    }
  }
}