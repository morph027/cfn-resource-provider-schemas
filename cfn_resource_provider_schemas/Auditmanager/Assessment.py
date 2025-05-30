SCHEMA = {
  "typeName" : "AWS::AuditManager::Assessment",
  "description" : "An entity that defines the scope of audit evidence collected by AWS Audit Manager.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "FrameworkId" : {
      "description" : "The identifier for the specified framework.",
      "type" : "string",
      "maxLength" : 36,
      "minLength" : 32,
      "pattern" : "^([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}|.*\\S.*)$"
    },
    "UUID" : {
      "type" : "string",
      "maxLength" : 36,
      "minLength" : 36,
      "pattern" : "^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$"
    },
    "AccountId" : {
      "description" : "The identifier for the specified AWS account.",
      "type" : "string",
      "maxLength" : 12,
      "minLength" : 12,
      "pattern" : "^[0-9]{12}$"
    },
    "EmailAddress" : {
      "description" : "The unique identifier for the email account.",
      "type" : "string",
      "maxLength" : 320,
      "minLength" : 1,
      "pattern" : "^.*@.*$"
    },
    "AccountName" : {
      "description" : "The name of the specified AWS account.",
      "type" : "string",
      "maxLength" : 50,
      "minLength" : 1,
      "pattern" : "^[\\u0020-\\u007E]+$"
    },
    "AWSAccount" : {
      "description" : "The AWS account associated with the assessment.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Id" : {
          "$ref" : "#/definitions/AccountId"
        },
        "EmailAddress" : {
          "$ref" : "#/definitions/EmailAddress"
        },
        "Name" : {
          "$ref" : "#/definitions/AccountName"
        }
      }
    },
    "AssessmentArn" : {
      "description" : "The Amazon Resource Name (ARN) of the assessment.",
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 20,
      "pattern" : "^arn:.*:auditmanager:.*"
    },
    "Timestamp" : {
      "description" : "The sequence of characters that identifies when the event occurred.",
      "type" : "number"
    },
    "ControlSetId" : {
      "description" : "The identifier for the specified control set.",
      "type" : "string",
      "maxLength" : 300,
      "minLength" : 1,
      "pattern" : "^[\\w\\W\\s\\S]*$"
    },
    "CreatedBy" : {
      "description" : "The IAM user or role that performed the action.",
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 20,
      "pattern" : "^arn:.*:*:.*"
    },
    "IamArn" : {
      "description" : "The Amazon Resource Name (ARN) of the IAM user or role.",
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 20,
      "pattern" : "^arn:.*:iam:.*"
    },
    "AssessmentName" : {
      "description" : "The name of the related assessment.",
      "type" : "string",
      "maxLength" : 127,
      "minLength" : 1,
      "pattern" : "^[a-zA-Z0-9-_\\.]+$"
    },
    "DelegationComment" : {
      "description" : "The comment related to the delegation.",
      "type" : "string",
      "maxLength" : 350,
      "pattern" : "^[\\w\\W\\s\\S]*$"
    },
    "RoleType" : {
      "description" : " The IAM role type.",
      "type" : "string",
      "enum" : [ "PROCESS_OWNER", "RESOURCE_OWNER" ]
    },
    "DelegationStatus" : {
      "description" : "The status of the delegation.",
      "type" : "string",
      "enum" : [ "IN_PROGRESS", "UNDER_REVIEW", "COMPLETE" ]
    },
    "Delegation" : {
      "description" : "The assignment of a control set to a delegate for review.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "LastUpdated" : {
          "$ref" : "#/definitions/Timestamp"
        },
        "ControlSetId" : {
          "$ref" : "#/definitions/ControlSetId"
        },
        "CreationTime" : {
          "$ref" : "#/definitions/Timestamp"
        },
        "CreatedBy" : {
          "$ref" : "#/definitions/CreatedBy"
        },
        "RoleArn" : {
          "$ref" : "#/definitions/IamArn"
        },
        "AssessmentName" : {
          "$ref" : "#/definitions/AssessmentName"
        },
        "Comment" : {
          "$ref" : "#/definitions/DelegationComment"
        },
        "Id" : {
          "$ref" : "#/definitions/UUID"
        },
        "RoleType" : {
          "$ref" : "#/definitions/RoleType"
        },
        "AssessmentId" : {
          "$ref" : "#/definitions/UUID"
        },
        "Status" : {
          "$ref" : "#/definitions/DelegationStatus"
        }
      }
    },
    "Role" : {
      "description" : "The wrapper that contains AWS Audit Manager role information, such as the role type and IAM ARN.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "RoleArn" : {
          "$ref" : "#/definitions/IamArn"
        },
        "RoleType" : {
          "$ref" : "#/definitions/RoleType"
        }
      }
    },
    "AWSServiceName" : {
      "description" : "The name of the AWS service.",
      "type" : "string"
    },
    "AWSService" : {
      "description" : "An AWS service such as Amazon S3, AWS CloudTrail, and so on.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ServiceName" : {
          "$ref" : "#/definitions/AWSServiceName"
        }
      }
    },
    "Scope" : {
      "description" : "The wrapper that contains the AWS accounts and AWS services in scope for the assessment.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "AwsAccounts" : {
          "description" : "The AWS accounts included in scope.",
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/AWSAccount"
          }
        },
        "AwsServices" : {
          "description" : "The AWS services included in scope.",
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/AWSService"
          }
        }
      }
    },
    "S3Url" : {
      "description" : "The URL of the specified Amazon S3 bucket.",
      "type" : "string"
    },
    "AssessmentReportDestinationType" : {
      "description" : "The destination type, such as Amazon S3.",
      "type" : "string",
      "enum" : [ "S3" ]
    },
    "AssessmentReportsDestination" : {
      "description" : "The destination in which evidence reports are stored for the specified assessment.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Destination" : {
          "$ref" : "#/definitions/S3Url"
        },
        "DestinationType" : {
          "$ref" : "#/definitions/AssessmentReportDestinationType"
        }
      }
    },
    "AssessmentStatus" : {
      "description" : "The status of the specified assessment. ",
      "type" : "string",
      "enum" : [ "ACTIVE", "INACTIVE" ]
    },
    "AssessmentDescription" : {
      "description" : "The description of the specified assessment.",
      "type" : "string"
    },
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ]
    }
  },
  "properties" : {
    "FrameworkId" : {
      "$ref" : "#/definitions/FrameworkId"
    },
    "AssessmentId" : {
      "$ref" : "#/definitions/UUID"
    },
    "AwsAccount" : {
      "$ref" : "#/definitions/AWSAccount"
    },
    "Arn" : {
      "$ref" : "#/definitions/AssessmentArn"
    },
    "Tags" : {
      "description" : "The tags associated with the assessment.",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "Delegations" : {
      "description" : "The list of delegations.",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Delegation"
      }
    },
    "Roles" : {
      "description" : "The list of roles for the specified assessment.",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Role"
      }
    },
    "Scope" : {
      "$ref" : "#/definitions/Scope"
    },
    "AssessmentReportsDestination" : {
      "$ref" : "#/definitions/AssessmentReportsDestination"
    },
    "Status" : {
      "$ref" : "#/definitions/AssessmentStatus"
    },
    "CreationTime" : {
      "$ref" : "#/definitions/Timestamp"
    },
    "Name" : {
      "$ref" : "#/definitions/AssessmentName"
    },
    "Description" : {
      "$ref" : "#/definitions/AssessmentDescription"
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "auditmanager:TagResource", "auditmanager:ListTagsForResource", "auditmanager:UntagResource" ]
  },
  "required" : [ ],
  "additionalProperties" : False,
  "readOnlyProperties" : [ "/properties/AssessmentId", "/properties/Arn", "/properties/CreationTime" ],
  "createOnlyProperties" : [ "/properties/FrameworkId", "/properties/AwsAccount" ],
  "writeOnlyProperties" : [ "/properties/Name", "/properties/Description" ],
  "primaryIdentifier" : [ "/properties/AssessmentId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "auditmanager:CreateAssessment", "auditmanager:TagResource", "auditmanager:ListTagsForResource", "auditmanager:BatchCreateDelegationByAssessment", "iam:PassRole" ]
    },
    "read" : {
      "permissions" : [ "auditmanager:GetAssessment" ]
    },
    "update" : {
      "permissions" : [ "auditmanager:UpdateAssessment", "auditmanager:UpdateAssessmentStatus", "auditmanager:BatchCreateDelegationByAssessment", "auditmanager:BatchDeleteDelegationByAssessment" ]
    },
    "delete" : {
      "permissions" : [ "auditmanager:DeleteAssessment", "auditmanager:UntagResource" ]
    },
    "list" : {
      "permissions" : [ "auditmanager:ListAssessments", "auditmanager:ListTagsForResource" ]
    }
  }
}