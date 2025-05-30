SCHEMA = {
  "typeName" : "AWS::RDS::Integration",
  "description" : "A zero-ETL integration with Amazon Redshift.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "properties" : {
    "IntegrationName" : {
      "description" : "The name of the integration.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 64
    },
    "Description" : {
      "type" : "string",
      "description" : "A description of the integration.",
      "minLength" : 1,
      "maxLength" : 1000
    },
    "Tags" : {
      "type" : "array",
      "maxItems" : 50,
      "uniqueItems" : True,
      "insertionOrder" : False,
      "description" : "A list of tags. For more information, see [Tagging Amazon RDS Resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide.*.",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "DataFilter" : {
      "type" : "string",
      "description" : "Data filters for the integration. These filters determine which tables from the source database are sent to the target Amazon Redshift data warehouse.",
      "minLength" : 1,
      "maxLength" : 25600,
      "pattern" : "[a-zA-Z0-9_ \"\\\\\\-$,*.:?+\\/]*"
    },
    "SourceArn" : {
      "type" : "string",
      "description" : "The Amazon Resource Name (ARN) of the database to use as the source for replication."
    },
    "TargetArn" : {
      "type" : "string",
      "description" : "The ARN of the Redshift data warehouse to use as the target for replication."
    },
    "IntegrationArn" : {
      "type" : "string",
      "description" : ""
    },
    "KMSKeyId" : {
      "type" : "string",
      "description" : "The AWS Key Management System (AWS KMS) key identifier for the key to use to encrypt the integration. If you don't specify an encryption key, RDS uses a default AWS owned key."
    },
    "AdditionalEncryptionContext" : {
      "$ref" : "#/definitions/EncryptionContextMap",
      "description" : "An optional set of non-secret key–value pairs that contains additional contextual information about the data. For more information, see [Encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context) in the *Key Management Service Developer Guide*.\n You can only include this parameter if you specify the ``KMSKeyId`` parameter."
    },
    "CreateTime" : {
      "type" : "string",
      "description" : ""
    }
  },
  "required" : [ "SourceArn", "TargetArn" ],
  "definitions" : {
    "Tags" : {
      "type" : "array",
      "maxItems" : 50,
      "uniqueItems" : True,
      "insertionOrder" : False,
      "description" : "An array of key-value pairs to apply to this resource.",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "Tag" : {
      "description" : "Metadata assigned to an Amazon RDS resource consisting of a key-value pair.\n For more information, see [Tagging Amazon RDS Resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS Resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can't be prefixed with ``aws:`` or ``rds:``. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', ':', '/', '=', '+', '-', '@' (Java regex: \"^([\\\\p{L}\\\\p{Z}\\\\p{N}_.:/=+\\\\-@]*)$\").",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can't be prefixed with ``aws:`` or ``rds:``. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', ':', '/', '=', '+', '-', '@' (Java regex: \"^([\\\\p{L}\\\\p{Z}\\\\p{N}_.:/=+\\\\-@]*)$\").",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key" ]
    },
    "EncryptionContextMap" : {
      "type" : "object",
      "patternProperties" : {
        "^[\\s\\S]*$" : {
          "type" : "string",
          "maxLength" : 131072,
          "minLength" : 0
        }
      },
      "description" : "An optional set of non-secret key–value pairs that contains additional contextual information about the data.",
      "additionalProperties" : False
    }
  },
  "propertyTransform" : {
    "/properties/SourceArn" : "$lowercase(SourceArn)",
    "/properties/KmsKeyId" : "$join([\"arn:(aws)[-]{0,1}[a-z]{0,2}[-]{0,1}[a-z]{0,3}:kms:[a-z]{2}[-]{1}[a-z]{3,10}[-]{0,1}[a-z]{0,10}[-]{1}[1-3]{1}:[0-9]{12}[:]{1}key\\/\", KmsKeyId])"
  },
  "createOnlyProperties" : [ "/properties/SourceArn", "/properties/TargetArn", "/properties/KMSKeyId", "/properties/AdditionalEncryptionContext" ],
  "readOnlyProperties" : [ "/properties/IntegrationArn", "/properties/CreateTime" ],
  "primaryIdentifier" : [ "/properties/IntegrationArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "rds:CreateIntegration", "rds:DescribeIntegrations", "rds:AddTagsToResource", "kms:CreateGrant", "kms:DescribeKey", "redshift:CreateInboundIntegration" ]
    },
    "read" : {
      "permissions" : [ "rds:DescribeIntegrations" ]
    },
    "update" : {
      "permissions" : [ "rds:DescribeIntegrations", "rds:AddTagsToResource", "rds:RemoveTagsFromResource", "rds:ModifyIntegration" ]
    },
    "delete" : {
      "permissions" : [ "rds:DeleteIntegration", "rds:DescribeIntegrations" ]
    },
    "list" : {
      "permissions" : [ "rds:DescribeIntegrations" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "rds:AddTagsToResource", "rds:RemoveTagsFromResource" ]
  },
  "additionalProperties" : False
}