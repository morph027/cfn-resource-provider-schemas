SCHEMA = {
  "typeName" : "AWS::Backup::RestoreTestingSelection",
  "description" : "Resource Type definition for AWS::Backup::RestoreTestingSelection",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "properties" : {
    "IamRoleArn" : {
      "type" : "string"
    },
    "ProtectedResourceArns" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "type" : "string"
      }
    },
    "ProtectedResourceConditions" : {
      "$ref" : "#/definitions/ProtectedResourceConditions"
    },
    "ProtectedResourceType" : {
      "type" : "string"
    },
    "RestoreMetadataOverrides" : {
      "$ref" : "#/definitions/SensitiveStringMap"
    },
    "RestoreTestingPlanName" : {
      "type" : "string"
    },
    "RestoreTestingSelectionName" : {
      "type" : "string"
    },
    "ValidationWindowHours" : {
      "type" : "integer"
    }
  },
  "required" : [ "IamRoleArn", "ProtectedResourceType", "RestoreTestingPlanName", "RestoreTestingSelectionName" ],
  "createOnlyProperties" : [ "/properties/ProtectedResourceType", "/properties/RestoreTestingPlanName", "/properties/RestoreTestingSelectionName" ],
  "replacementStrategy" : "delete_then_create",
  "primaryIdentifier" : [ "/properties/RestoreTestingPlanName", "/properties/RestoreTestingSelectionName" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "additionalProperties" : False,
  "definitions" : {
    "KeyValue" : {
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string"
        },
        "Value" : {
          "type" : "string"
        }
      },
      "required" : [ "Key", "Value" ],
      "type" : "object"
    },
    "ProtectedResourceConditions" : {
      "additionalProperties" : False,
      "properties" : {
        "StringEquals" : {
          "type" : "array",
          "insertionOrder" : False,
          "items" : {
            "$ref" : "#/definitions/KeyValue"
          }
        },
        "StringNotEquals" : {
          "type" : "array",
          "insertionOrder" : False,
          "items" : {
            "$ref" : "#/definitions/KeyValue"
          }
        }
      },
      "type" : "object"
    },
    "SensitiveStringMap" : {
      "additionalProperties" : False,
      "patternProperties" : {
        ".+" : {
          "type" : "string"
        }
      },
      "type" : "object"
    }
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "backup:CreateRestoreTestingSelection", "backup:GetRestoreTestingSelection", "iam:PassRole" ],
      "timeoutInMinutes" : 5
    },
    "read" : {
      "permissions" : [ "backup:GetRestoreTestingSelection" ],
      "timeoutInMinutes" : 5
    },
    "update" : {
      "permissions" : [ "backup:UpdateRestoreTestingSelection", "backup:GetRestoreTestingSelection", "iam:PassRole" ],
      "timeoutInMinutes" : 5
    },
    "delete" : {
      "permissions" : [ "backup:DeleteRestoreTestingSelection", "backup:GetRestoreTestingSelection" ],
      "timeoutInMinutes" : 5
    },
    "list" : {
      "permissions" : [ "backup:ListRestoreTestingSelections", "backup:ListRestoreTestingPlans" ],
      "timeoutInMinutes" : 5
    }
  }
}