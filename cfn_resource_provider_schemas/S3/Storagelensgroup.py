SCHEMA = {
  "typeName" : "AWS::S3::StorageLensGroup",
  "description" : "The AWS::S3::StorageLensGroup resource is an Amazon S3 resource type that you can use to create Storage Lens Group.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-s3-storagelensgroup",
  "definitions" : {
    "Name" : {
      "description" : "The name that identifies the Amazon S3 Storage Lens Group.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 64,
      "pattern" : "^[a-zA-Z0-9\\-_]+$"
    },
    "MatchAnyPrefix" : {
      "description" : "Filter to match any of the specified prefixes.",
      "type" : "array",
      "insertionOrder" : False,
      "uniqueItems" : True,
      "items" : {
        "type" : "string",
        "maxLength" : 1024
      }
    },
    "MatchAnySuffix" : {
      "description" : "Filter to match any of the specified suffixes.",
      "type" : "array",
      "insertionOrder" : False,
      "uniqueItems" : True,
      "items" : {
        "type" : "string",
        "maxLength" : 1024
      }
    },
    "MatchAnyTag" : {
      "description" : "Filter to match any of the specified object tags.",
      "type" : "array",
      "insertionOrder" : False,
      "uniqueItems" : True,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "MatchObjectAge" : {
      "description" : "Filter to match all of the specified values for the minimum and maximum object age.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "DaysGreaterThan" : {
          "description" : "Minimum object age to which the rule applies.",
          "type" : "integer",
          "minimum" : 1
        },
        "DaysLessThan" : {
          "description" : "Maximum object age to which the rule applies.",
          "type" : "integer",
          "minimum" : 1
        }
      }
    },
    "MatchObjectSize" : {
      "description" : "Filter to match all of the specified values for the minimum and maximum object size.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "BytesGreaterThan" : {
          "description" : "Minimum object size to which the rule applies.",
          "type" : "integer",
          "format" : "int64",
          "minimum" : 1
        },
        "BytesLessThan" : {
          "description" : "Maximum object size to which the rule applies.",
          "type" : "integer",
          "format" : "int64",
          "minimum" : 1
        }
      }
    },
    "And" : {
      "description" : "The Storage Lens group will include objects that match all of the specified filter values.",
      "type" : "object",
      "uniqueItems" : True,
      "additionalProperties" : False,
      "minProperties" : 2,
      "properties" : {
        "MatchAnyPrefix" : {
          "$ref" : "#/definitions/MatchAnyPrefix"
        },
        "MatchAnySuffix" : {
          "$ref" : "#/definitions/MatchAnySuffix"
        },
        "MatchAnyTag" : {
          "$ref" : "#/definitions/MatchAnyTag"
        },
        "MatchObjectSize" : {
          "$ref" : "#/definitions/MatchObjectSize"
        },
        "MatchObjectAge" : {
          "$ref" : "#/definitions/MatchObjectAge"
        }
      }
    },
    "Or" : {
      "description" : "The Storage Lens group will include objects that match any of the specified filter values.",
      "type" : "object",
      "uniqueItems" : True,
      "additionalProperties" : False,
      "minProperties" : 2,
      "properties" : {
        "MatchAnyPrefix" : {
          "$ref" : "#/definitions/MatchAnyPrefix"
        },
        "MatchAnySuffix" : {
          "$ref" : "#/definitions/MatchAnySuffix"
        },
        "MatchAnyTag" : {
          "$ref" : "#/definitions/MatchAnyTag"
        },
        "MatchObjectSize" : {
          "$ref" : "#/definitions/MatchObjectSize"
        },
        "MatchObjectAge" : {
          "$ref" : "#/definitions/MatchObjectAge"
        }
      }
    },
    "Filter" : {
      "description" : "Sets the Storage Lens Group filter.",
      "type" : "object",
      "properties" : {
        "MatchAnyPrefix" : {
          "$ref" : "#/definitions/MatchAnyPrefix"
        },
        "MatchAnySuffix" : {
          "$ref" : "#/definitions/MatchAnySuffix"
        },
        "MatchAnyTag" : {
          "$ref" : "#/definitions/MatchAnyTag"
        },
        "MatchObjectSize" : {
          "$ref" : "#/definitions/MatchObjectSize"
        },
        "MatchObjectAge" : {
          "$ref" : "#/definitions/MatchObjectAge"
        },
        "And" : {
          "$ref" : "#/definitions/And"
        },
        "Or" : {
          "$ref" : "#/definitions/Or"
        }
      },
      "additionalProperties" : False
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
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ]
    }
  },
  "properties" : {
    "Name" : {
      "$ref" : "#/definitions/Name"
    },
    "Filter" : {
      "$ref" : "#/definitions/Filter"
    },
    "StorageLensGroupArn" : {
      "description" : "The ARN for the Amazon S3 Storage Lens Group.",
      "type" : "string"
    },
    "Tags" : {
      "description" : "A set of tags (key-value pairs) for this Amazon S3 Storage Lens Group.",
      "type" : "array",
      "insertionOrder" : True,
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "required" : [ "Name", "Filter" ],
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags"
  },
  "readOnlyProperties" : [ "/properties/StorageLensGroupArn" ],
  "createOnlyProperties" : [ "/properties/Name" ],
  "primaryIdentifier" : [ "/properties/Name" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "s3:CreateStorageLensGroup", "s3:GetStorageLensGroup", "s3:TagResource", "s3:ListTagsForResource" ]
    },
    "read" : {
      "permissions" : [ "s3:GetStorageLensGroup", "s3:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "s3:GetStorageLensGroup", "s3:UpdateStorageLensGroup", "s3:TagResource", "s3:UntagResource", "s3:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "s3:DeleteStorageLensGroup" ]
    },
    "list" : {
      "permissions" : [ "s3:ListStorageLensGroups" ]
    }
  }
}