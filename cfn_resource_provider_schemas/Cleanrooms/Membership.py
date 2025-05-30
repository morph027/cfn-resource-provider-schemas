SCHEMA = {
  "typeName" : "AWS::CleanRooms::Membership",
  "description" : "Represents an AWS account that is a part of a collaboration",
  "definitions" : {
    "MembershipQueryLogStatus" : {
      "type" : "string",
      "enum" : [ "ENABLED", "DISABLED" ]
    },
    "MembershipJobLogStatus" : {
      "type" : "string",
      "enum" : [ "ENABLED", "DISABLED" ]
    },
    "MembershipStatus" : {
      "type" : "string",
      "enum" : [ "ACTIVE", "REMOVED", "COLLABORATION_DELETED" ]
    },
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
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
      "required" : [ "Value", "Key" ]
    },
    "ResultFormat" : {
      "type" : "string",
      "enum" : [ "CSV", "PARQUET" ]
    },
    "ProtectedQueryS3OutputConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ResultFormat" : {
          "$ref" : "#/definitions/ResultFormat"
        },
        "Bucket" : {
          "type" : "string",
          "minLength" : 3,
          "maxLength" : 63
        },
        "KeyPrefix" : {
          "type" : "string"
        },
        "SingleFileOutput" : {
          "type" : "boolean"
        }
      },
      "required" : [ "ResultFormat", "Bucket" ]
    },
    "ProtectedJobS3OutputConfigurationInput" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Bucket" : {
          "type" : "string",
          "minLength" : 3,
          "maxLength" : 63
        },
        "KeyPrefix" : {
          "type" : "string"
        }
      },
      "required" : [ "Bucket" ]
    },
    "MembershipProtectedQueryOutputConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "S3" : {
          "$ref" : "#/definitions/ProtectedQueryS3OutputConfiguration"
        }
      },
      "required" : [ "S3" ]
    },
    "MembershipProtectedJobOutputConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "S3" : {
          "$ref" : "#/definitions/ProtectedJobS3OutputConfigurationInput"
        }
      },
      "required" : [ "S3" ]
    },
    "MembershipProtectedQueryResultConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "OutputConfiguration" : {
          "$ref" : "#/definitions/MembershipProtectedQueryOutputConfiguration"
        },
        "RoleArn" : {
          "type" : "string",
          "minLength" : 32,
          "maxLength" : 512
        }
      },
      "required" : [ "OutputConfiguration" ]
    },
    "MembershipProtectedJobResultConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "OutputConfiguration" : {
          "$ref" : "#/definitions/MembershipProtectedJobOutputConfiguration"
        },
        "RoleArn" : {
          "type" : "string",
          "minLength" : 32,
          "maxLength" : 512
        }
      },
      "required" : [ "OutputConfiguration", "RoleArn" ]
    },
    "MembershipPaymentConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "QueryCompute" : {
          "$ref" : "#/definitions/MembershipQueryComputePaymentConfig"
        },
        "MachineLearning" : {
          "$ref" : "#/definitions/MembershipMLPaymentConfig"
        },
        "JobCompute" : {
          "$ref" : "#/definitions/MembershipJobComputePaymentConfig"
        }
      },
      "required" : [ "QueryCompute" ]
    },
    "MembershipQueryComputePaymentConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "IsResponsible" : {
          "type" : "boolean"
        }
      },
      "required" : [ "IsResponsible" ]
    },
    "MembershipMLPaymentConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ModelTraining" : {
          "$ref" : "#/definitions/MembershipModelTrainingPaymentConfig"
        },
        "ModelInference" : {
          "$ref" : "#/definitions/MembershipModelInferencePaymentConfig"
        }
      }
    },
    "MembershipModelTrainingPaymentConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "IsResponsible" : {
          "type" : "boolean"
        }
      },
      "required" : [ "IsResponsible" ]
    },
    "MembershipModelInferencePaymentConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "IsResponsible" : {
          "type" : "boolean"
        }
      },
      "required" : [ "IsResponsible" ]
    },
    "MembershipJobComputePaymentConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "IsResponsible" : {
          "type" : "boolean"
        }
      },
      "required" : [ "IsResponsible" ]
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string",
      "maxLength" : 100
    },
    "Tags" : {
      "description" : "An arbitrary set of tags (key-value pairs) for this cleanrooms membership.",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "uniqueItems" : True,
      "type" : "array"
    },
    "CollaborationArn" : {
      "type" : "string",
      "maxLength" : 100
    },
    "CollaborationCreatorAccountId" : {
      "type" : "string",
      "maxLength" : 12,
      "minLength" : 12,
      "pattern" : "^\\d+$"
    },
    "CollaborationIdentifier" : {
      "type" : "string",
      "maxLength" : 36,
      "minLength" : 36,
      "pattern" : "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
    },
    "MembershipIdentifier" : {
      "type" : "string",
      "maxLength" : 36,
      "minLength" : 36,
      "pattern" : "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
    },
    "QueryLogStatus" : {
      "$ref" : "#/definitions/MembershipQueryLogStatus"
    },
    "JobLogStatus" : {
      "$ref" : "#/definitions/MembershipJobLogStatus"
    },
    "DefaultResultConfiguration" : {
      "$ref" : "#/definitions/MembershipProtectedQueryResultConfiguration"
    },
    "DefaultJobResultConfiguration" : {
      "$ref" : "#/definitions/MembershipProtectedJobResultConfiguration"
    },
    "PaymentConfiguration" : {
      "$ref" : "#/definitions/MembershipPaymentConfiguration"
    }
  },
  "required" : [ "CollaborationIdentifier", "QueryLogStatus" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/CollaborationArn", "/properties/CollaborationCreatorAccountId", "/properties/MembershipIdentifier" ],
  "createOnlyProperties" : [ "/properties/CollaborationIdentifier" ],
  "primaryIdentifier" : [ "/properties/MembershipIdentifier" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "cleanrooms:ListTagsForResource", "cleanrooms:UntagResource", "cleanrooms:TagResource" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "cleanrooms:CreateMembership", "logs:CreateLogDelivery", "logs:GetLogDelivery", "logs:UpdateLogDelivery", "logs:DeleteLogDelivery", "logs:ListLogDeliveries", "logs:DescribeLogGroups", "logs:DescribeResourcePolicies", "logs:PutResourcePolicy", "logs:CreateLogGroup", "cleanrooms:GetMembership", "cleanrooms:ListTagsForResource", "cleanrooms:TagResource", "cleanrooms:ListMemberships", "iam:PassRole" ]
    },
    "read" : {
      "permissions" : [ "cleanrooms:GetMembership", "cleanrooms:ListTagsForResource", "logs:ListLogDeliveries", "logs:DescribeLogGroups", "logs:DescribeResourcePolicies", "logs:GetLogDelivery" ]
    },
    "update" : {
      "permissions" : [ "cleanrooms:UpdateMembership", "cleanrooms:GetMembership", "logs:CreateLogDelivery", "logs:GetLogDelivery", "logs:UpdateLogDelivery", "logs:DeleteLogDelivery", "logs:ListLogDeliveries", "logs:DescribeLogGroups", "logs:DescribeResourcePolicies", "logs:PutResourcePolicy", "logs:CreateLogGroup", "cleanrooms:ListTagsForResource", "cleanrooms:TagResource", "cleanrooms:UntagResource", "iam:PassRole" ]
    },
    "delete" : {
      "permissions" : [ "cleanrooms:DeleteMembership", "cleanrooms:GetMembership", "cleanrooms:ListMemberships", "cleanrooms:ListTagsForResource", "logs:ListLogDeliveries", "logs:DescribeLogGroups", "logs:DescribeResourcePolicies", "logs:GetLogDelivery" ]
    },
    "list" : {
      "permissions" : [ "cleanrooms:ListMemberships" ]
    }
  },
  "additionalProperties" : False
}