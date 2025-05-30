SCHEMA = {
  "tagging" : {
    "permissions" : [ "entityresolution:TagResource", "entityresolution:UntagResource", "entityresolution:ListTagsForResource" ],
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "tagProperty" : "/properties/Tags",
    "cloudFormationSystemTags" : True
  },
  "typeName" : "AWS::EntityResolution::IdMappingWorkflow",
  "readOnlyProperties" : [ "/properties/WorkflowArn", "/properties/UpdatedAt", "/properties/CreatedAt" ],
  "description" : "IdMappingWorkflow defined in AWS Entity Resolution service",
  "createOnlyProperties" : [ "/properties/WorkflowName" ],
  "primaryIdentifier" : [ "/properties/WorkflowName" ],
  "required" : [ "WorkflowName", "InputSourceConfig", "IdMappingTechniques", "RoleArn" ],
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-entity-resolution.git",
  "handlers" : {
    "read" : {
      "permissions" : [ "entityresolution:GetIdMappingWorkflow", "entityresolution:ListTagsForResource" ]
    },
    "create" : {
      "permissions" : [ "entityresolution:CreateIdMappingWorkflow", "entityresolution:GetIdMappingWorkflow", "entityresolution:TagResource", "kms:CreateGrant", "kms:DescribeKey", "iam:PassRole" ]
    },
    "update" : {
      "permissions" : [ "entityresolution:GetIdMappingWorkflow", "entityresolution:UpdateIdMappingWorkflow", "entityresolution:ListTagsForResource", "entityresolution:TagResource", "entityresolution:UntagResource", "iam:PassRole", "kms:CreateGrant", "kms:DescribeKey" ]
    },
    "list" : {
      "permissions" : [ "entityresolution:ListIdMappingWorkflows" ]
    },
    "delete" : {
      "permissions" : [ "entityresolution:DeleteIdMappingWorkflow", "entityresolution:GetIdMappingWorkflow", "entityresolution:UntagResource" ]
    }
  },
  "writeOnlyProperties" : [ "/properties/IdMappingTechniques/NormalizationVersion" ],
  "additionalProperties" : False,
  "definitions" : {
    "IdMappingWorkflowOutputSource" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "KMSArn" : {
          "$ref" : "#/definitions/KMSArn"
        },
        "OutputS3Path" : {
          "pattern" : "^s3://([^/]+)/?(.*?([^/]+)/?)$",
          "description" : "The S3 path to which Entity Resolution will write the output table",
          "type" : "string"
        }
      },
      "required" : [ "OutputS3Path" ]
    },
    "Description" : {
      "minLength" : 0,
      "type" : "string",
      "maxLength" : 255
    },
    "IdMappingWorkflowInputSource" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "Type" : {
          "type" : "string",
          "enum" : [ "SOURCE", "TARGET" ]
        },
        "InputSourceARN" : {
          "pattern" : "^arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(idnamespace/[a-zA-Z_0-9-]{1,255})$|^arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(matchingworkflow/[a-zA-Z_0-9-]{1,255})$|^arn:(aws|aws-us-gov|aws-cn):glue:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(table/[a-zA-Z_0-9-]{1,255}/[a-zA-Z_0-9-]{1,255})$",
          "description" : "An Glue table ARN for the input source table, MatchingWorkflow arn or IdNamespace ARN",
          "type" : "string"
        },
        "SchemaArn" : {
          "type" : "string",
          "$ref" : "#/definitions/SchemaMappingArn"
        }
      },
      "required" : [ "InputSourceARN" ]
    },
    "EntityName" : {
      "minLength" : 0,
      "pattern" : "^[a-zA-Z_0-9-]*$",
      "type" : "string",
      "maxLength" : 255
    },
    "IdMappingTechniques" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "RuleBasedProperties" : {
          "$ref" : "#/definitions/IdMappingRuleBasedProperties"
        },
        "ProviderProperties" : {
          "$ref" : "#/definitions/ProviderProperties"
        },
        "IdMappingType" : {
          "type" : "string",
          "enum" : [ "PROVIDER", "RULE_BASED" ]
        }
      }
    },
    "CreatedAt" : {
      "description" : "The time of this IdMappingWorkflow got created",
      "type" : "string"
    },
    "IdMappingWorkflowArn" : {
      "pattern" : "^arn:(aws|aws-us-gov|aws-cn):entityresolution:.*:[0-9]+:(idmappingworkflow/.*)$",
      "description" : "The default IdMappingWorkflow arn",
      "type" : "string"
    },
    "UpdatedAt" : {
      "description" : "The time of this IdMappingWorkflow got last updated at",
      "type" : "string"
    },
    "IdMappingRuleBasedProperties" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "AttributeMatchingModel" : {
          "type" : "string",
          "enum" : [ "ONE_TO_ONE", "MANY_TO_MANY" ]
        },
        "RuleDefinitionType" : {
          "type" : "string",
          "enum" : [ "SOURCE", "TARGET" ]
        },
        "Rules" : {
          "minItems" : 1,
          "maxItems" : 25,
          "insertionOrder" : False,
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/Rule"
          }
        },
        "RecordMatchingModel" : {
          "type" : "string",
          "enum" : [ "ONE_SOURCE_TO_ONE_TARGET", "MANY_SOURCE_TO_ONE_TARGET" ]
        }
      },
      "required" : [ "AttributeMatchingModel", "RecordMatchingModel" ]
    },
    "KMSArn" : {
      "pattern" : "^arn:(aws|aws-us-gov|aws-cn):kms:.*:[0-9]+:.*$",
      "type" : "string"
    },
    "ProviderProperties" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "IntermediateSourceConfiguration" : {
          "$ref" : "#/definitions/IntermediateSourceConfiguration"
        },
        "ProviderServiceArn" : {
          "pattern" : "^arn:(aws|aws-us-gov|aws-cn):(entityresolution):([a-z]{2}-[a-z]{1,10}-[0-9])::providerservice/([a-zA-Z0-9_-]{1,255})/([a-zA-Z0-9_-]{1,255})$",
          "description" : "Arn of the Provider Service being used.",
          "type" : "string"
        },
        "ProviderConfiguration" : {
          "patternProperties" : {
            "^.+$" : {
              "type" : "string"
            }
          },
          "description" : "Additional Provider configuration that would be required for the provider service. The Configuration must be in JSON string format",
          "additionalProperties" : False,
          "type" : "object"
        }
      },
      "required" : [ "ProviderServiceArn" ]
    },
    "IntermediateSourceConfiguration" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "IntermediateS3Path" : {
          "description" : "The s3 path that would be used to stage the intermediate data being generated during workflow execution.",
          "type" : "string"
        }
      },
      "required" : [ "IntermediateS3Path" ]
    },
    "SchemaMappingArn" : {
      "pattern" : "^arn:(aws|aws-us-gov|aws-cn):entityresolution:.*:[0-9]+:(schemamapping/.*)$",
      "description" : "The SchemaMapping arn associated with the Schema",
      "type" : "string"
    },
    "AttributeName" : {
      "minLength" : 0,
      "pattern" : "^[a-zA-Z_0-9- \\t]*$",
      "type" : "string",
      "maxLength" : 255
    },
    "Rule" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "MatchingKeys" : {
          "minItems" : 1,
          "maxItems" : 15,
          "insertionOrder" : False,
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/AttributeName"
          }
        },
        "RuleName" : {
          "minLength" : 0,
          "pattern" : "^[a-zA-Z_0-9- \\t]*$",
          "type" : "string",
          "maxLength" : 255
        }
      },
      "required" : [ "RuleName", "MatchingKeys" ]
    },
    "Tag" : {
      "description" : "A key-value pair to associate with a resource",
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "Value" : {
          "minLength" : 0,
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "type" : "string",
          "maxLength" : 256
        },
        "Key" : {
          "minLength" : 1,
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "type" : "string",
          "maxLength" : 128
        }
      },
      "required" : [ "Key", "Value" ]
    }
  },
  "properties" : {
    "Description" : {
      "description" : "The description of the IdMappingWorkflow",
      "$ref" : "#/definitions/Description"
    },
    "InputSourceConfig" : {
      "minItems" : 1,
      "maxItems" : 20,
      "insertionOrder" : False,
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/IdMappingWorkflowInputSource"
      }
    },
    "IdMappingTechniques" : {
      "$ref" : "#/definitions/IdMappingTechniques"
    },
    "WorkflowName" : {
      "description" : "The name of the IdMappingWorkflow",
      "$ref" : "#/definitions/EntityName"
    },
    "CreatedAt" : {
      "$ref" : "#/definitions/CreatedAt"
    },
    "OutputSourceConfig" : {
      "minItems" : 1,
      "maxItems" : 1,
      "insertionOrder" : False,
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/IdMappingWorkflowOutputSource"
      }
    },
    "WorkflowArn" : {
      "$ref" : "#/definitions/IdMappingWorkflowArn"
    },
    "UpdatedAt" : {
      "$ref" : "#/definitions/UpdatedAt"
    },
    "RoleArn" : {
      "pattern" : "^arn:(aws|aws-us-gov|aws-cn):iam::\\d{12}:role/?[a-zA-Z_0-9+=,.@\\-_/]+$",
      "type" : "string"
    },
    "Tags" : {
      "minItems" : 0,
      "maxItems" : 200,
      "uniqueItems" : True,
      "insertionOrder" : False,
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  }
}