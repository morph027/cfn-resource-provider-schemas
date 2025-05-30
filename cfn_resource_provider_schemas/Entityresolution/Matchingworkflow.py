SCHEMA = {
  "typeName" : "AWS::EntityResolution::MatchingWorkflow",
  "description" : "MatchingWorkflow defined in AWS Entity Resolution service",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-entity-resolution.git",
  "definitions" : {
    "EntityName" : {
      "type" : "string",
      "pattern" : "^[a-zA-Z_0-9-]*$",
      "minLength" : 0,
      "maxLength" : 255
    },
    "Description" : {
      "type" : "string",
      "minLength" : 0,
      "maxLength" : 255
    },
    "AttributeName" : {
      "type" : "string",
      "pattern" : "^[a-zA-Z_0-9- \\t]*$",
      "minLength" : 0,
      "maxLength" : 255
    },
    "SchemaMappingArn" : {
      "description" : "The SchemaMapping arn associated with the Schema",
      "type" : "string",
      "pattern" : "^arn:(aws|aws-us-gov|aws-cn):entityresolution:.*:[0-9]+:(schemamapping/.*)$"
    },
    "KMSArn" : {
      "type" : "string",
      "pattern" : "^arn:(aws|aws-us-gov|aws-cn):kms:.*:[0-9]+:.*$"
    },
    "MatchingWorkflowArn" : {
      "description" : "The default MatchingWorkflow arn",
      "type" : "string",
      "pattern" : "^arn:(aws|aws-us-gov|aws-cn):entityresolution:.*:[0-9]+:(matchingworkflow/.*)$"
    },
    "CreatedAt" : {
      "description" : "The time of this MatchingWorkflow got created",
      "type" : "string"
    },
    "UpdatedAt" : {
      "description" : "The time of this MatchingWorkflow got last updated at",
      "type" : "string"
    },
    "InputSource" : {
      "type" : "object",
      "properties" : {
        "InputSourceARN" : {
          "description" : "An Glue table ARN for the input source table",
          "type" : "string",
          "pattern" : "arn:(aws|aws-us-gov|aws-cn):.*:.*:[0-9]+:.*$"
        },
        "SchemaArn" : {
          "type" : "string",
          "$ref" : "#/definitions/SchemaMappingArn"
        },
        "ApplyNormalization" : {
          "type" : "boolean"
        }
      },
      "required" : [ "InputSourceARN", "SchemaArn" ],
      "additionalProperties" : False
    },
    "OutputSource" : {
      "type" : "object",
      "properties" : {
        "OutputS3Path" : {
          "description" : "The S3 path to which Entity Resolution will write the output table",
          "type" : "string",
          "pattern" : "^s3://([^/]+)/?(.*?([^/]+)/?)$"
        },
        "Output" : {
          "type" : "array",
          "insertionOrder" : False,
          "minItems" : 0,
          "maxItems" : 750,
          "items" : {
            "$ref" : "#/definitions/OutputAttribute"
          }
        },
        "KMSArn" : {
          "$ref" : "#/definitions/KMSArn"
        },
        "ApplyNormalization" : {
          "type" : "boolean"
        }
      },
      "required" : [ "Output", "OutputS3Path" ],
      "additionalProperties" : False
    },
    "OutputAttribute" : {
      "type" : "object",
      "properties" : {
        "Name" : {
          "$ref" : "#/definitions/AttributeName"
        },
        "Hashed" : {
          "type" : "boolean"
        }
      },
      "required" : [ "Name" ],
      "additionalProperties" : False
    },
    "ResolutionType" : {
      "type" : "string",
      "enum" : [ "RULE_MATCHING", "ML_MATCHING", "PROVIDER" ]
    },
    "ResolutionTechniques" : {
      "type" : "object",
      "properties" : {
        "ResolutionType" : {
          "$ref" : "#/definitions/ResolutionType"
        },
        "RuleBasedProperties" : {
          "$ref" : "#/definitions/RuleBasedProperties"
        },
        "ProviderProperties" : {
          "$ref" : "#/definitions/ProviderProperties"
        }
      },
      "additionalProperties" : False
    },
    "IncrementalRunConfig" : {
      "type" : "object",
      "properties" : {
        "IncrementalRunType" : {
          "type" : "string",
          "enum" : [ "IMMEDIATE" ]
        }
      },
      "required" : [ "IncrementalRunType" ],
      "additionalProperties" : False
    },
    "RuleBasedProperties" : {
      "type" : "object",
      "properties" : {
        "Rules" : {
          "type" : "array",
          "insertionOrder" : False,
          "minItems" : 1,
          "maxItems" : 15,
          "items" : {
            "$ref" : "#/definitions/Rule"
          }
        },
        "AttributeMatchingModel" : {
          "type" : "string",
          "enum" : [ "ONE_TO_ONE", "MANY_TO_MANY" ]
        },
        "MatchPurpose" : {
          "type" : "string",
          "enum" : [ "IDENTIFIER_GENERATION", "INDEXING" ]
        }
      },
      "required" : [ "AttributeMatchingModel", "Rules" ],
      "additionalProperties" : False
    },
    "Rule" : {
      "type" : "object",
      "properties" : {
        "RuleName" : {
          "type" : "string",
          "pattern" : "^[a-zA-Z_0-9- \\t]*$",
          "minLength" : 0,
          "maxLength" : 255
        },
        "MatchingKeys" : {
          "type" : "array",
          "insertionOrder" : False,
          "minItems" : 1,
          "maxItems" : 15,
          "items" : {
            "$ref" : "#/definitions/AttributeName"
          }
        }
      },
      "required" : [ "RuleName", "MatchingKeys" ],
      "additionalProperties" : False
    },
    "ProviderProperties" : {
      "type" : "object",
      "properties" : {
        "ProviderServiceArn" : {
          "type" : "string",
          "description" : "Arn of the Provider service being used."
        },
        "ProviderConfiguration" : {
          "type" : "object",
          "additionalProperties" : False,
          "patternProperties" : {
            "^.+$" : {
              "type" : "string"
            }
          },
          "description" : "Additional Provider configuration that would be required for the provider service. The Configuration must be in JSON string format"
        },
        "IntermediateSourceConfiguration" : {
          "$ref" : "#/definitions/IntermediateSourceConfiguration"
        }
      },
      "required" : [ "ProviderServiceArn" ],
      "additionalProperties" : False
    },
    "IntermediateSourceConfiguration" : {
      "type" : "object",
      "properties" : {
        "IntermediateS3Path" : {
          "type" : "string",
          "description" : "The s3 path that would be used to stage the intermediate data being generated during workflow execution."
        }
      },
      "required" : [ "IntermediateS3Path" ],
      "additionalProperties" : False
    },
    "Tag" : {
      "description" : "A key-value pair to associate with a resource",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "WorkflowName" : {
      "description" : "The name of the MatchingWorkflow",
      "$ref" : "#/definitions/EntityName"
    },
    "Description" : {
      "description" : "The description of the MatchingWorkflow",
      "$ref" : "#/definitions/Description"
    },
    "InputSourceConfig" : {
      "type" : "array",
      "insertionOrder" : False,
      "minItems" : 1,
      "maxItems" : 20,
      "items" : {
        "$ref" : "#/definitions/InputSource"
      }
    },
    "OutputSourceConfig" : {
      "type" : "array",
      "insertionOrder" : False,
      "minItems" : 1,
      "maxItems" : 1,
      "items" : {
        "$ref" : "#/definitions/OutputSource"
      }
    },
    "ResolutionTechniques" : {
      "$ref" : "#/definitions/ResolutionTechniques"
    },
    "RoleArn" : {
      "type" : "string",
      "pattern" : "^arn:(aws|aws-us-gov|aws-cn):iam::\\d{12}:role/?[a-zA-Z_0-9+=,.@\\-_/]+$"
    },
    "Tags" : {
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "minItems" : 0,
      "maxItems" : 200,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "WorkflowArn" : {
      "$ref" : "#/definitions/MatchingWorkflowArn"
    },
    "CreatedAt" : {
      "$ref" : "#/definitions/CreatedAt"
    },
    "UpdatedAt" : {
      "$ref" : "#/definitions/UpdatedAt"
    },
    "IncrementalRunConfig" : {
      "$ref" : "#/definitions/IncrementalRunConfig"
    }
  },
  "createOnlyProperties" : [ "/properties/WorkflowName" ],
  "readOnlyProperties" : [ "/properties/WorkflowArn", "/properties/UpdatedAt", "/properties/CreatedAt" ],
  "primaryIdentifier" : [ "/properties/WorkflowName" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "entityresolution:TagResource", "entityresolution:UntagResource", "entityresolution:ListTagsForResource" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "entityresolution:CreateMatchingWorkflow", "entityresolution:GetMatchingWorkflow", "entityresolution:TagResource", "kms:CreateGrant", "kms:DescribeKey", "iam:PassRole", "events:PutRule", "events:DeleteRule", "events:PutTargets", "events:ListTargetsByRule" ]
    },
    "read" : {
      "permissions" : [ "entityresolution:GetMatchingWorkflow", "entityresolution:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "entityresolution:DeleteMatchingWorkflow", "entityresolution:GetMatchingWorkflow", "entityresolution:UntagResource", "events:PutRule", "events:DeleteRule", "events:PutTargets", "events:RemoveTargets", "events:ListTargetsByRule" ]
    },
    "list" : {
      "permissions" : [ "entityresolution:ListMatchingWorkflows" ]
    },
    "update" : {
      "permissions" : [ "entityresolution:GetMatchingWorkflow", "entityresolution:UpdateMatchingWorkflow", "entityresolution:ListTagsForResource", "entityresolution:TagResource", "entityresolution:UntagResource", "iam:PassRole", "kms:CreateGrant", "kms:DescribeKey", "events:PutRule", "events:DeleteRule", "events:PutTargets", "events:RemoveTargets", "events:ListTargetsByRule" ]
    }
  },
  "required" : [ "WorkflowName", "InputSourceConfig", "OutputSourceConfig", "ResolutionTechniques", "RoleArn" ],
  "additionalProperties" : False
}