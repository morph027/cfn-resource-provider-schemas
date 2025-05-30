SCHEMA = {
  "typeName" : "AWS::SES::MailManagerArchive",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-ses-mailmanager",
  "description" : "Definition of AWS::SES::MailManagerArchive Resource Type",
  "definitions" : {
    "ArchiveRetention" : {
      "oneOf" : [ {
        "type" : "object",
        "title" : "RetentionPeriod",
        "properties" : {
          "RetentionPeriod" : {
            "$ref" : "#/definitions/RetentionPeriod"
          }
        },
        "required" : [ "RetentionPeriod" ],
        "additionalProperties" : False
      } ]
    },
    "ArchiveState" : {
      "type" : "string",
      "enum" : [ "ACTIVE", "PENDING_DELETION" ]
    },
    "RetentionPeriod" : {
      "type" : "string",
      "enum" : [ "THREE_MONTHS", "SIX_MONTHS", "NINE_MONTHS", "ONE_YEAR", "EIGHTEEN_MONTHS", "TWO_YEARS", "THIRTY_MONTHS", "THREE_YEARS", "FOUR_YEARS", "FIVE_YEARS", "SIX_YEARS", "SEVEN_YEARS", "EIGHT_YEARS", "NINE_YEARS", "TEN_YEARS", "PERMANENT" ]
    },
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 1,
          "pattern" : "^[a-zA-Z0-9/_\\+=\\.:@\\-]+$"
        },
        "Value" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0,
          "pattern" : "^[a-zA-Z0-9/_\\+=\\.:@\\-]*$"
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "ArchiveArn" : {
      "type" : "string"
    },
    "ArchiveId" : {
      "type" : "string",
      "maxLength" : 66,
      "minLength" : 1
    },
    "ArchiveName" : {
      "type" : "string",
      "maxLength" : 64,
      "minLength" : 1,
      "pattern" : "^[a-zA-Z0-9][a-zA-Z0-9_-]*[a-zA-Z0-9]$"
    },
    "ArchiveState" : {
      "$ref" : "#/definitions/ArchiveState"
    },
    "KmsKeyArn" : {
      "type" : "string",
      "pattern" : "^arn:aws(|-cn|-us-gov):kms:[a-z0-9-]{1,20}:[0-9]{12}:(key|alias)/.+$"
    },
    "Retention" : {
      "$ref" : "#/definitions/ArchiveRetention"
    },
    "Tags" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "maxItems" : 200,
      "minItems" : 0
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "ses:TagResource", "ses:UntagResource" ]
  },
  "readOnlyProperties" : [ "/properties/ArchiveArn", "/properties/ArchiveId", "/properties/ArchiveState" ],
  "createOnlyProperties" : [ "/properties/KmsKeyArn" ],
  "primaryIdentifier" : [ "/properties/ArchiveId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ses:TagResource", "ses:ListTagsForResource", "ses:GetArchive", "ses:CreateArchive", "kms:DescribeKey", "kms:Decrypt", "kms:GenerateDataKey" ]
    },
    "read" : {
      "permissions" : [ "ses:ListTagsForResource", "ses:GetArchive" ]
    },
    "update" : {
      "permissions" : [ "ses:TagResource", "ses:UntagResource", "ses:ListTagsForResource", "ses:GetArchive", "ses:UpdateArchive" ]
    },
    "delete" : {
      "permissions" : [ "ses:GetArchive", "ses:DeleteArchive" ]
    },
    "list" : {
      "permissions" : [ "ses:ListArchives" ]
    }
  },
  "additionalProperties" : False
}