SCHEMA = {
  "typeName" : "AWS::Location::Tracker",
  "description" : "Definition of AWS::Location::Tracker Resource Type",
  "definitions" : {
    "PositionFiltering" : {
      "type" : "string",
      "enum" : [ "TimeBased", "DistanceBased", "AccuracyBased" ]
    },
    "PricingPlan" : {
      "type" : "string",
      "enum" : [ "RequestBasedUsage" ]
    },
    "TagMap" : {
      "type" : "object",
      "maxProperties" : 50,
      "patternProperties" : {
        "^([\\p{L}\\p{Z}\\p{N}_.,:/=+\\-@]*)$" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0,
          "pattern" : "^([\\p{L}\\p{Z}\\p{N}_.,:/=+\\-@]*)$"
        }
      },
      "additionalProperties" : False
    },
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 1,
          "maxLength" : 128,
          "pattern" : "^[a-zA-Z+-=._:/]+$"
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 0,
          "maxLength" : 256,
          "pattern" : "^[A-Za-z0-9 _=@:.+-/]*$"
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    },
    "iso8601UTC" : {
      "description" : "The datetime value in ISO 8601 format. The timezone is always UTC. (YYYY-MM-DDThh:mm:ss.sssZ)",
      "type" : "string",
      "pattern" : "^([0-2]\\d{3})-(0[0-9]|1[0-2])-([0-2]\\d|3[01])T([01]\\d|2[0-4]):([0-5]\\d):([0-6]\\d)((\\.\\d{3})?)Z$"
    }
  },
  "properties" : {
    "CreateTime" : {
      "$ref" : "#/definitions/iso8601UTC"
    },
    "Description" : {
      "type" : "string",
      "maxLength" : 1000,
      "minLength" : 0
    },
    "EventBridgeEnabled" : {
      "type" : "boolean"
    },
    "KmsKeyEnableGeospatialQueries" : {
      "type" : "boolean"
    },
    "KmsKeyId" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 1
    },
    "PositionFiltering" : {
      "$ref" : "#/definitions/PositionFiltering"
    },
    "PricingPlan" : {
      "$ref" : "#/definitions/PricingPlan"
    },
    "PricingPlanDataSource" : {
      "type" : "string",
      "description" : "This shape is deprecated since 2022-02-01: Deprecated. No longer allowed."
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this resource.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "minItems" : 0,
      "maxItems" : 200,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "TrackerArn" : {
      "type" : "string",
      "maxLength" : 1600,
      "pattern" : "^arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:([^/].*)?$"
    },
    "TrackerName" : {
      "type" : "string",
      "maxLength" : 100,
      "minLength" : 1,
      "pattern" : "^[-._\\w]+$"
    },
    "UpdateTime" : {
      "$ref" : "#/definitions/iso8601UTC"
    },
    "Arn" : {
      "type" : "string",
      "maxLength" : 1600,
      "pattern" : "^arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:([^/].*)?$"
    }
  },
  "readOnlyProperties" : [ "/properties/CreateTime", "/properties/Arn", "/properties/TrackerArn", "/properties/UpdateTime" ],
  "createOnlyProperties" : [ "/properties/KmsKeyId", "/properties/TrackerName" ],
  "deprecatedProperties" : [ "/properties/PricingPlan", "/properties/PricingPlanDataSource" ],
  "primaryIdentifier" : [ "/properties/TrackerName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "geo:CreateTracker", "geo:DescribeTracker", "geo:TagResource", "geo:UntagResource", "kms:DescribeKey", "kms:CreateGrant" ]
    },
    "read" : {
      "permissions" : [ "geo:DescribeTracker", "kms:DescribeKey" ]
    },
    "update" : {
      "permissions" : [ "geo:CreateTracker", "geo:DescribeTracker", "geo:TagResource", "geo:UntagResource", "kms:DescribeKey", "kms:CreateGrant", "geo:UpdateTracker" ]
    },
    "delete" : {
      "permissions" : [ "geo:DeleteTracker", "geo:DescribeTracker" ]
    },
    "list" : {
      "permissions" : [ "geo:ListTrackers" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "geo:TagResource", "geo:UntagResource" ]
  },
  "required" : [ "TrackerName" ],
  "additionalProperties" : False
}