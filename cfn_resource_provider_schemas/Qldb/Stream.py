SCHEMA = {
  "typeName" : "AWS::QLDB::Stream",
  "description" : "Resource schema for AWS::QLDB::Stream.",
  "additionalProperties" : False,
  "definitions" : {
    "Arn" : {
      "type" : "string",
      "pattern" : "arn:[\\w+=/,.@-]+:[\\w+=/,.@-]+:[\\w+=/,.@-]*:[0-9]*:[\\w+=,.@-]+(/[\\w+=,.@-]+)*"
    },
    "KinesisConfiguration" : {
      "type" : "object",
      "properties" : {
        "StreamArn" : {
          "type" : "object",
          "$ref" : "#/definitions/Arn"
        },
        "AggregationEnabled" : {
          "type" : "boolean"
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
          "description" : "The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "minLength" : 1,
          "maxLength" : 127
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "minLength" : 1,
          "maxLength" : 255
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "qldb:TagResource", "qldb:UntagResource", "qldb:ListTagsForResource" ]
  },
  "properties" : {
    "LedgerName" : {
      "type" : "string"
    },
    "StreamName" : {
      "type" : "string"
    },
    "RoleArn" : {
      "$ref" : "#/definitions/Arn"
    },
    "InclusiveStartTime" : {
      "type" : "string"
    },
    "ExclusiveEndTime" : {
      "type" : "string"
    },
    "KinesisConfiguration" : {
      "$ref" : "#/definitions/KinesisConfiguration"
    },
    "Tags" : {
      "type" : "array",
      "maxItems" : 50,
      "insertionOrder" : False,
      "uniqueItems" : True,
      "description" : "An array of key-value pairs to apply to this resource.",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "Arn" : {
      "$ref" : "#/definitions/Arn"
    },
    "Id" : {
      "type" : "string"
    }
  },
  "required" : [ "LedgerName", "StreamName", "RoleArn", "KinesisConfiguration", "InclusiveStartTime" ],
  "createOnlyProperties" : [ "/properties/LedgerName", "/properties/StreamName", "/properties/RoleArn", "/properties/KinesisConfiguration", "/properties/InclusiveStartTime", "/properties/ExclusiveEndTime" ],
  "primaryIdentifier" : [ "/properties/LedgerName", "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id", "/properties/Arn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iam:PassRole", "qldb:StreamJournalToKinesis", "qldb:DescribeJournalKinesisStream" ]
    },
    "delete" : {
      "permissions" : [ "qldb:CancelJournalKinesisStream", "qldb:DescribeJournalKinesisStream" ]
    },
    "read" : {
      "permissions" : [ "qldb:DescribeJournalKinesisStream", "qldb:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "qldb:DescribeJournalKinesisStream", "qldb:UntagResource", "qldb:TagResource" ]
    },
    "list" : {
      "permissions" : [ "qldb:listJournalKinesisStreamsForLedger" ],
      "handlerSchema" : {
        "properties" : {
          "LedgerName" : {
            "type" : "string"
          }
        },
        "required" : [ "LedgerName" ]
      }
    }
  }
}