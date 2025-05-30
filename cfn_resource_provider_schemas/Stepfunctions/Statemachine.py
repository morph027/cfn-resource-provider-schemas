SCHEMA = {
  "typeName" : "AWS::StepFunctions::StateMachine",
  "description" : "Resource schema for StateMachine",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-stepfunctions.git",
  "definitions" : {
    "TagsEntry" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 256
        }
      },
      "additionalProperties" : False,
      "required" : [ "Key", "Value" ]
    },
    "CloudWatchLogsLogGroup" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "LogGroupArn" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 256
        }
      }
    },
    "LogDestination" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "CloudWatchLogsLogGroup" : {
          "$ref" : "#/definitions/CloudWatchLogsLogGroup"
        }
      }
    },
    "LoggingConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Level" : {
          "type" : "string",
          "enum" : [ "ALL", "ERROR", "FATAL", "OFF" ]
        },
        "IncludeExecutionData" : {
          "type" : "boolean"
        },
        "Destinations" : {
          "type" : "array",
          "minItems" : 1,
          "insertionOrder" : False,
          "items" : {
            "$ref" : "#/definitions/LogDestination"
          }
        }
      }
    },
    "TracingConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Enabled" : {
          "type" : "boolean"
        }
      }
    },
    "EncryptionConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "KmsKeyId" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 2048
        },
        "KmsDataKeyReusePeriodSeconds" : {
          "type" : "integer",
          "minimum" : 60,
          "maximum" : 900
        },
        "Type" : {
          "type" : "string",
          "enum" : [ "CUSTOMER_MANAGED_KMS_KEY", "AWS_OWNED_KEY" ]
        }
      },
      "required" : [ "Type" ]
    },
    "S3Location" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Bucket" : {
          "type" : "string"
        },
        "Key" : {
          "type" : "string"
        },
        "Version" : {
          "type" : "string"
        }
      },
      "required" : [ "Bucket", "Key" ]
    },
    "DefinitionSubstitutions" : {
      "type" : "object",
      "additionalProperties" : False,
      "patternProperties" : {
        ".*" : {
          "anyOf" : [ {
            "type" : "string"
          }, {
            "type" : "integer"
          }, {
            "type" : "boolean"
          } ]
        }
      },
      "minProperties" : 1
    },
    "Definition" : {
      "type" : "object",
      "minProperties" : 1
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 2048
    },
    "Name" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 80
    },
    "DefinitionString" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 1048576
    },
    "RoleArn" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 256
    },
    "StateMachineName" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 80
    },
    "StateMachineType" : {
      "type" : "string",
      "enum" : [ "STANDARD", "EXPRESS" ]
    },
    "StateMachineRevisionId" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 256
    },
    "LoggingConfiguration" : {
      "$ref" : "#/definitions/LoggingConfiguration"
    },
    "TracingConfiguration" : {
      "$ref" : "#/definitions/TracingConfiguration"
    },
    "EncryptionConfiguration" : {
      "$ref" : "#/definitions/EncryptionConfiguration"
    },
    "DefinitionS3Location" : {
      "$ref" : "#/definitions/S3Location"
    },
    "DefinitionSubstitutions" : {
      "$ref" : "#/definitions/DefinitionSubstitutions"
    },
    "Definition" : {
      "$ref" : "#/definitions/Definition"
    },
    "Tags" : {
      "type" : "array",
      "uniqueItems" : False,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/TagsEntry"
      }
    }
  },
  "required" : [ "RoleArn" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "states:UntagResource", "states:TagResource", "states:ListTagsForResource" ]
  },
  "additionalProperties" : False,
  "readOnlyProperties" : [ "/properties/Arn", "/properties/Name", "/properties/StateMachineRevisionId" ],
  "createOnlyProperties" : [ "/properties/StateMachineName", "/properties/StateMachineType" ],
  "writeOnlyProperties" : [ "/properties/Definition", "/properties/DefinitionS3Location", "/properties/DefinitionSubstitutions" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "additionalIdentifiers" : [ [ "/properties/StateMachineName" ] ],
  "handlers" : {
    "create" : {
      "permissions" : [ "states:CreateStateMachine", "states:DescribeStateMachine", "states:TagResource", "iam:PassRole", "s3:GetObject", "kms:DescribeKey", "kms:GenerateDataKey" ]
    },
    "read" : {
      "permissions" : [ "states:DescribeStateMachine", "states:ListTagsForResource", "kms:Decrypt" ]
    },
    "update" : {
      "permissions" : [ "states:UpdateStateMachine", "states:TagResource", "states:UntagResource", "states:ListTagsForResource", "iam:PassRole", "kms:DescribeKey", "kms:GenerateDataKey" ]
    },
    "delete" : {
      "permissions" : [ "states:DeleteStateMachine", "states:DescribeStateMachine" ]
    },
    "list" : {
      "permissions" : [ "states:ListStateMachines" ]
    }
  }
}