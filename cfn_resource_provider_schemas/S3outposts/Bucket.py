SCHEMA = {
  "typeName" : "AWS::S3Outposts::Bucket",
  "description" : "Resource Type Definition for AWS::S3Outposts::Bucket",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-s3outposts.git",
  "definitions" : {
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 1024,
          "pattern" : "^(?!aws:.*)([\\p{L}\\p{Z}\\p{N}_.:=+\\/\\-@%]*)$"
        },
        "Value" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 1024,
          "pattern" : "^([\\p{L}\\p{Z}\\p{N}_.:=+\\/\\-@%]*)$"
        }
      },
      "required" : [ "Key", "Value" ]
    },
    "LifecycleConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Rules" : {
          "description" : "A list of lifecycle rules for individual objects in an Amazon S3Outposts bucket.",
          "type" : "array",
          "insertionOrder" : False,
          "uniqueItems" : True,
          "items" : {
            "$ref" : "#/definitions/Rule"
          }
        }
      },
      "required" : [ "Rules" ]
    },
    "Rule" : {
      "description" : "Specifies lifecycle rules for an Amazon S3Outposts bucket. You must specify at least one of the following: AbortIncompleteMultipartUpload, ExpirationDate, ExpirationInDays.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Status" : {
          "type" : "string",
          "enum" : [ "Enabled", "Disabled" ]
        },
        "Id" : {
          "type" : "string",
          "maxLength" : 255,
          "description" : "Unique identifier for the lifecycle rule. The value can't be longer than 255 characters."
        },
        "AbortIncompleteMultipartUpload" : {
          "description" : "Specifies a lifecycle rule that stops incomplete multipart uploads to an Amazon S3Outposts bucket.",
          "$ref" : "#/definitions/AbortIncompleteMultipartUpload"
        },
        "ExpirationDate" : {
          "description" : "Indicates when objects are deleted from Amazon S3Outposts. The date value must be in ISO 8601 format. The time is always midnight UTC.",
          "$ref" : "#/definitions/iso8601UTC"
        },
        "ExpirationInDays" : {
          "description" : "Indicates the number of days after creation when objects are deleted from Amazon S3Outposts.",
          "type" : "integer",
          "minimum" : 1
        },
        "Filter" : {
          "description" : "The container for the filter of the lifecycle rule.",
          "type" : "object",
          "additionalProperties" : False,
          "properties" : {
            "Prefix" : {
              "description" : "Object key prefix that identifies one or more objects to which this rule applies.",
              "$ref" : "#/definitions/FilterPrefix"
            },
            "Tag" : {
              "description" : "Specifies a tag used to identify a subset of objects for an Amazon S3Outposts bucket.",
              "$ref" : "#/definitions/FilterTag"
            },
            "AndOperator" : {
              "description" : "The container for the AND condition for the lifecycle rule. A combination of Prefix and 1 or more Tags OR a minimum of 2 or more tags.",
              "$ref" : "#/definitions/FilterAndOperator"
            }
          },
          "oneOf" : [ {
            "required" : [ "Prefix" ]
          }, {
            "required" : [ "Tag" ]
          }, {
            "required" : [ "AndOperator" ]
          } ]
        }
      },
      "anyOf" : [ {
        "required" : [ "Status", "AbortIncompleteMultipartUpload" ]
      }, {
        "required" : [ "Status", "ExpirationDate" ]
      }, {
        "required" : [ "Status", "ExpirationInDays" ]
      } ]
    },
    "iso8601UTC" : {
      "description" : "The date value in ISO 8601 format. The timezone is always UTC. (YYYY-MM-DDThh:mm:ssZ)",
      "type" : "string",
      "pattern" : "^([0-2]\\d{3})-(0[0-9]|1[0-2])-([0-2]\\d|3[01])T([01]\\d|2[0-4]):([0-5]\\d):([0-6]\\d)((\\.\\d{3})?)Z$"
    },
    "AbortIncompleteMultipartUpload" : {
      "description" : "Specifies the days since the initiation of an incomplete multipart upload that Amazon S3Outposts will wait before permanently removing all parts of the upload.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "DaysAfterInitiation" : {
          "description" : "Specifies the number of days after which Amazon S3Outposts aborts an incomplete multipart upload.",
          "type" : "integer",
          "minimum" : 0
        }
      },
      "required" : [ "DaysAfterInitiation" ]
    },
    "FilterPrefix" : {
      "description" : "Prefix identifies one or more objects to which the rule applies.",
      "type" : "string"
    },
    "FilterTag" : {
      "description" : "Tag used to identify a subset of objects for an Amazon S3Outposts bucket.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 1024,
          "pattern" : "^([\\p{L}\\p{Z}\\p{N}_.:=+\\/\\-@%]*)$"
        },
        "Value" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 1024,
          "pattern" : "^([\\p{L}\\p{Z}\\p{N}_.:=+\\/\\-@%]*)$"
        }
      },
      "required" : [ "Key", "Value" ]
    },
    "FilterAndOperator" : {
      "oneOf" : [ {
        "type" : "object",
        "additionalProperties" : False,
        "required" : [ "Tags" ],
        "properties" : {
          "Prefix" : {
            "description" : "Prefix identifies one or more objects to which the rule applies.",
            "$ref" : "#/definitions/FilterPrefix"
          },
          "Tags" : {
            "description" : "All of these tags must exist in the object's tag set in order for the rule to apply.",
            "type" : "array",
            "insertionOrder" : False,
            "uniqueItems" : True,
            "minItems" : 1,
            "items" : {
              "$ref" : "#/definitions/FilterTag"
            }
          }
        }
      } ]
    }
  },
  "properties" : {
    "Arn" : {
      "description" : "The Amazon Resource Name (ARN) of the specified bucket.",
      "maxLength" : 2048,
      "minLength" : 20,
      "pattern" : "^arn:[^:]+:s3-outposts:[a-zA-Z0-9\\-]+:\\d{12}:outpost\\/[^:]+\\/bucket\\/[^:]+$",
      "type" : "string"
    },
    "BucketName" : {
      "description" : "A name for the bucket.",
      "maxLength" : 63,
      "minLength" : 3,
      "pattern" : "(?=^.{3,63}$)(?!^(\\d+\\.)+\\d+$)(^(([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])\\.)*([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])$)",
      "type" : "string"
    },
    "OutpostId" : {
      "description" : "The id of the customer outpost on which the bucket resides.",
      "pattern" : "^(op-[a-f0-9]{17}|\\d{12}|ec2)$",
      "type" : "string"
    },
    "Tags" : {
      "description" : "An arbitrary set of tags (key-value pairs) for this S3Outposts bucket.",
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "type" : "array",
      "insertionOrder" : False,
      "uniqueItems" : True
    },
    "LifecycleConfiguration" : {
      "description" : "Rules that define how Amazon S3Outposts manages objects during their lifetime.",
      "$ref" : "#/definitions/LifecycleConfiguration"
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "s3-outposts:DeleteBucketTagging", "s3-outposts:PutBucketTagging", "s3-outposts:GetBucketTagging" ]
  },
  "additionalProperties" : False,
  "createOnlyProperties" : [ "/properties/BucketName", "/properties/OutpostId" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "required" : [ "BucketName", "OutpostId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "s3-outposts:CreateBucket", "s3-outposts:PutBucketTagging", "s3-outposts:PutLifecycleConfiguration" ]
    },
    "read" : {
      "permissions" : [ "s3-outposts:GetBucket", "s3-outposts:GetBucketTagging", "s3-outposts:GetLifecycleConfiguration" ]
    },
    "update" : {
      "permissions" : [ "s3-outposts:PutBucketTagging", "s3-outposts:DeleteBucketTagging", "s3-outposts:PutLifecycleConfiguration" ]
    },
    "delete" : {
      "permissions" : [ "s3-outposts:DeleteBucket" ]
    },
    "list" : {
      "permissions" : [ "s3-outposts:ListRegionalBuckets" ],
      "handlerSchema" : {
        "properties" : {
          "OutpostId" : {
            "$ref" : "resource-schema.json#/properties/OutpostId"
          }
        },
        "required" : [ "OutpostId" ]
      }
    }
  }
}