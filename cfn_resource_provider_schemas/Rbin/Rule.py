SCHEMA = {
  "typeName" : "AWS::Rbin::Rule",
  "description" : "Resource Type definition for AWS::Rbin::Rule",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-rbin",
  "definitions" : {
    "Tag" : {
      "description" : "Metadata of a retention rule, consisting of a key-value pair.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "description" : "A unique identifier for the tag.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "description" : "String which you can use to describe or define the tag.",
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ]
    },
    "ResourceTag" : {
      "description" : "The resource tag of the rule.",
      "type" : "object",
      "properties" : {
        "ResourceTagKey" : {
          "description" : "The tag key of the resource.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "ResourceTagValue" : {
          "description" : "The tag value of the resource",
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "additionalProperties" : False,
      "required" : [ "ResourceTagKey", "ResourceTagValue" ]
    },
    "RetentionPeriod" : {
      "description" : "The retention period of the rule.",
      "type" : "object",
      "properties" : {
        "RetentionPeriodValue" : {
          "description" : "The retention period value of the rule.",
          "type" : "integer",
          "minimum" : 1,
          "maximum" : 3650
        },
        "RetentionPeriodUnit" : {
          "description" : "The retention period unit of the rule",
          "type" : "string",
          "enum" : [ "DAYS" ]
        }
      },
      "additionalProperties" : False,
      "required" : [ "RetentionPeriodValue", "RetentionPeriodUnit" ]
    },
    "UnlockDelay" : {
      "type" : "object",
      "properties" : {
        "UnlockDelayValue" : {
          "description" : "The unlock delay period, measured in the unit specified for UnlockDelayUnit.",
          "type" : "integer",
          "minimum" : 7,
          "maximum" : 30
        },
        "UnlockDelayUnit" : {
          "description" : "The unit of time in which to measure the unlock delay. Currently, the unlock delay can be measure only in days.",
          "type" : "string",
          "enum" : [ "DAYS" ]
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Arn" : {
      "description" : "Rule Arn is unique for each rule.",
      "type" : "string",
      "minLength" : 0,
      "maxLength" : 1011
    },
    "Identifier" : {
      "description" : "The unique ID of the retention rule.",
      "type" : "string",
      "pattern" : "[0-9a-zA-Z]{11}"
    },
    "Description" : {
      "description" : "The description of the retention rule.",
      "type" : "string",
      "maxLength" : 255
    },
    "ResourceTags" : {
      "description" : "Information about the resource tags used to identify resources that are retained by the retention rule.",
      "type" : "array",
      "maxItems" : 50,
      "insertionOrder" : False,
      "uniqueItems" : True,
      "items" : {
        "$ref" : "#/definitions/ResourceTag"
      }
    },
    "ExcludeResourceTags" : {
      "description" : "Information about the exclude resource tags used to identify resources that are excluded by the retention rule.",
      "type" : "array",
      "maxItems" : 5,
      "insertionOrder" : False,
      "uniqueItems" : True,
      "items" : {
        "$ref" : "#/definitions/ResourceTag"
      }
    },
    "ResourceType" : {
      "description" : "The resource type retained by the retention rule.",
      "type" : "string",
      "enum" : [ "EBS_SNAPSHOT", "EC2_IMAGE" ]
    },
    "Tags" : {
      "description" : "Information about the tags assigned to the retention rule.",
      "type" : "array",
      "maxItems" : 200,
      "insertionOrder" : False,
      "uniqueItems" : True,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "RetentionPeriod" : {
      "description" : "Information about the retention period for which the retention rule is to retain resources.",
      "$ref" : "#/definitions/RetentionPeriod"
    },
    "Status" : {
      "description" : "The state of the retention rule. Only retention rules that are in the available state retain resources.",
      "type" : "string",
      "pattern" : "pending|available"
    },
    "LockConfiguration" : {
      "description" : "Information about the retention rule lock configuration.",
      "$ref" : "#/definitions/UnlockDelay"
    },
    "LockState" : {
      "description" : "The lock state for the retention rule.",
      "type" : "string",
      "pattern" : "locked|pending_unlock|unlocked"
    }
  },
  "additionalProperties" : False,
  "required" : [ "RetentionPeriod", "ResourceType" ],
  "createOnlyProperties" : [ "/properties/ResourceType" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/Identifier", "/properties/LockState" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "writeOnlyProperties" : [ "/properties/LockConfiguration", "/properties/LockConfiguration/UnlockDelayValue", "/properties/LockConfiguration/UnlockDelayUnit" ],
  "additionalIdentifiers" : [ [ "/properties/Identifier" ] ],
  "handlers" : {
    "create" : {
      "permissions" : [ "rbin:CreateRule", "rbin:GetRule", "rbin:LockRule", "rbin:TagResource", "iam:PassRole" ]
    },
    "read" : {
      "permissions" : [ "rbin:GetRule", "rbin:ListTagsForResource", "iam:PassRole" ]
    },
    "update" : {
      "permissions" : [ "rbin:GetRule", "rbin:UpdateRule", "rbin:LockRule", "rbin:UnlockRule", "rbin:TagResource", "rbin:UntagResource", "rbin:ListTagsForResource", "iam:PassRole" ]
    },
    "delete" : {
      "permissions" : [ "rbin:GetRule", "rbin:DeleteRule", "iam:PassRole" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "LockState" : {
            "$ref" : "resource-schema.json#/properties/LockState"
          },
          "ResourceTags" : {
            "$ref" : "resource-schema.json#/properties/ResourceTags"
          },
          "ExcludeResourceTags" : {
            "$ref" : "resource-schema.json#/properties/ExcludeResourceTags"
          },
          "ResourceType" : {
            "$ref" : "resource-schema.json#/properties/ResourceType"
          }
        },
        "required" : [ "ResourceType" ]
      },
      "permissions" : [ "rbin:ListRules", "rbin:ListTagsForResource", "iam:PassRole" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "rbin:TagResource", "rbin:UntagResource", "rbin:ListTagsForResource" ]
  }
}