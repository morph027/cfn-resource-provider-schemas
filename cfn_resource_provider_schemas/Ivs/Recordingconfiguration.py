SCHEMA = {
  "typeName" : "AWS::IVS::RecordingConfiguration",
  "description" : "Resource Type definition for AWS::IVS::RecordingConfiguration",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
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
      "required" : [ "Value", "Key" ]
    },
    "DestinationConfiguration" : {
      "description" : "Recording Destination Configuration.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "S3" : {
          "$ref" : "#/definitions/S3DestinationConfiguration"
        }
      },
      "required" : [ ]
    },
    "S3DestinationConfiguration" : {
      "description" : "Recording S3 Destination Configuration.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "BucketName" : {
          "type" : "string",
          "minLength" : 3,
          "maxLength" : 63,
          "pattern" : "^[a-z0-9-.]+$"
        }
      },
      "required" : [ "BucketName" ]
    },
    "ThumbnailConfiguration" : {
      "description" : "Recording Thumbnail Configuration.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "RecordingMode" : {
          "description" : "Thumbnail Recording Mode, which determines whether thumbnails are recorded at an interval or are disabled.",
          "type" : "string",
          "enum" : [ "INTERVAL", "DISABLED" ],
          "default" : "INTERVAL"
        },
        "TargetIntervalSeconds" : {
          "description" : "Target Interval Seconds defines the interval at which thumbnails are recorded. This field is required if RecordingMode is INTERVAL.",
          "type" : "integer",
          "minimum" : 1,
          "maximum" : 60,
          "default" : 60
        },
        "Resolution" : {
          "description" : "Resolution indicates the desired resolution of recorded thumbnails.",
          "type" : "string",
          "enum" : [ "FULL_HD", "HD", "SD", "LOWEST_RESOLUTION" ]
        },
        "Storage" : {
          "description" : "Storage indicates the format in which thumbnails are recorded.",
          "type" : "array",
          "uniqueItems" : True,
          "insertionOrder" : False,
          "minItems" : 0,
          "maxItems" : 2,
          "items" : {
            "type" : "string",
            "enum" : [ "SEQUENTIAL", "LATEST" ]
          }
        }
      },
      "required" : [ ]
    },
    "RenditionConfiguration" : {
      "description" : "Rendition Configuration describes which renditions should be recorded for a stream.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "RenditionSelection" : {
          "description" : "Resolution Selection indicates which set of renditions are recorded for a stream.",
          "type" : "string",
          "enum" : [ "ALL", "NONE", "CUSTOM" ],
          "default" : "ALL"
        },
        "Renditions" : {
          "description" : "Renditions indicates which renditions are recorded for a stream.",
          "type" : "array",
          "uniqueItems" : True,
          "insertionOrder" : False,
          "minItems" : 0,
          "maxItems" : 4,
          "items" : {
            "type" : "string",
            "enum" : [ "FULL_HD", "HD", "SD", "LOWEST_RESOLUTION" ]
          }
        }
      },
      "required" : [ ]
    }
  },
  "properties" : {
    "Arn" : {
      "description" : "Recording Configuration ARN is automatically generated on creation and assigned as the unique identifier.",
      "type" : "string",
      "pattern" : "^arn:aws[-a-z]*:ivs:[a-z0-9-]+:[0-9]+:recording-configuration/[a-zA-Z0-9-]+$",
      "minLength" : 0,
      "maxLength" : 128
    },
    "Name" : {
      "description" : "Recording Configuration Name.",
      "type" : "string",
      "minLength" : 0,
      "maxLength" : 128,
      "pattern" : "^[a-zA-Z0-9-_]*$"
    },
    "State" : {
      "description" : "Recording Configuration State.",
      "type" : "string",
      "enum" : [ "CREATING", "CREATE_FAILED", "ACTIVE" ]
    },
    "RecordingReconnectWindowSeconds" : {
      "description" : "Recording Reconnect Window Seconds. (0 means disabled)",
      "type" : "integer",
      "default" : 0,
      "minimum" : 0,
      "maximum" : 300
    },
    "DestinationConfiguration" : {
      "$ref" : "#/definitions/DestinationConfiguration"
    },
    "Tags" : {
      "description" : "A list of key-value pairs that contain metadata for the asset model.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "maxItems" : 50,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "ThumbnailConfiguration" : {
      "$ref" : "#/definitions/ThumbnailConfiguration"
    },
    "RenditionConfiguration" : {
      "$ref" : "#/definitions/RenditionConfiguration"
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "ivs:TagResource", "ivs:UntagResource", "ivs:ListTagsForResource" ]
  },
  "required" : [ "DestinationConfiguration" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/State" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/DestinationConfiguration", "/properties/DestinationConfiguration/S3", "/properties/DestinationConfiguration/S3/BucketName", "/properties/RecordingReconnectWindowSeconds", "/properties/ThumbnailConfiguration", "/properties/ThumbnailConfiguration/RecordingMode", "/properties/ThumbnailConfiguration/TargetIntervalSeconds", "/properties/ThumbnailConfiguration/Storage", "/properties/ThumbnailConfiguration/Resolution", "/properties/RenditionConfiguration", "/properties/RenditionConfiguration/RenditionSelection", "/properties/RenditionConfiguration/Renditions" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ivs:CreateRecordingConfiguration", "ivs:GetRecordingConfiguration", "ivs:TagResource", "iam:CreateServiceLinkedRole", "iam:PutRolePolicy", "iam:AttachRolePolicy", "s3:ListBucket", "s3:GetBucketLocation", "cloudformation:ListExports" ]
    },
    "read" : {
      "permissions" : [ "ivs:GetRecordingConfiguration", "s3:GetBucketLocation", "ivs:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "ivs:GetRecordingConfiguration", "sts:AssumeRole", "iam:CreateServiceLinkedRole", "iam:PutRolePolicy", "iam:AttachRolePolicy", "s3:ListBucket", "ivs:TagResource", "ivs:UntagResource", "ivs:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "ivs:DeleteRecordingConfiguration", "ivs:UntagResource", "iam:CreateServiceLinkedRole" ]
    },
    "list" : {
      "permissions" : [ "ivs:ListRecordingConfigurations", "s3:GetBucketLocation", "ivs:ListTagsForResource" ]
    }
  }
}