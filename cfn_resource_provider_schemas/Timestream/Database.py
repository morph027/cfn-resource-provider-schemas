SCHEMA = {
  "typeName" : "AWS::Timestream::Database",
  "description" : "The AWS::Timestream::Database resource creates a Timestream database.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-timestream.git",
  "definitions" : {
    "Tag" : {
      "description" : "You can use the Resource Tags property to apply tags to resources, which can help you identify and categorize those resources.",
      "type" : "object",
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
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string"
    },
    "DatabaseName" : {
      "description" : "The name for the database. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the database name.",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9_.-]{3,256}$"
    },
    "KmsKeyId" : {
      "description" : "The KMS key for the database. If the KMS key is not specified, the database will be encrypted with a Timestream managed KMS key located in your account.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 2048
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this resource.",
      "type" : "array",
      "maxItems" : 200,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/DatabaseName" ],
  "createOnlyProperties" : [ "/properties/DatabaseName" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "timestream:TagResource", "timestream:ListTagsForResource", "timestream:UntagResource" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "timestream:CreateDatabase", "timestream:DescribeEndpoints", "timestream:TagResource", "kms:CreateGrant", "kms:DescribeKey", "kms:Decrypt" ]
    },
    "read" : {
      "permissions" : [ "timestream:DescribeDatabase", "timestream:DescribeEndpoints", "timestream:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "timestream:UpdateDatabase", "timestream:DescribeDatabase", "timestream:DescribeEndpoints", "timestream:TagResource", "timestream:UntagResource" ]
    },
    "delete" : {
      "permissions" : [ "timestream:DeleteDatabase", "timestream:DescribeEndpoints" ]
    },
    "list" : {
      "permissions" : [ "timestream:ListDatabases", "timestream:DescribeEndpoints" ]
    }
  }
}