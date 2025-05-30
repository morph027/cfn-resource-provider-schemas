SCHEMA = {
  "typeName" : "AWS::Redshift::Integration",
  "description" : "Integration from a source AWS service to a Redshift cluster",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "properties" : {
    "IntegrationArn" : {
      "type" : "string",
      "description" : "The Amazon Resource Name (ARN) of the integration."
    },
    "IntegrationName" : {
      "description" : "The name of the integration.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 64
    },
    "SourceArn" : {
      "type" : "string",
      "description" : "The Amazon Resource Name (ARN) of the database to use as the source for replication"
    },
    "TargetArn" : {
      "type" : "string",
      "description" : "The Amazon Resource Name (ARN) of the Redshift data warehouse to use as the target for replication"
    },
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
    "CreateTime" : {
      "type" : "string",
      "description" : "The time (UTC) when the integration was created."
    },
    "KMSKeyId" : {
      "type" : "string",
      "description" : "An KMS key identifier for the key to use to encrypt the integration. If you don't specify an encryption key, the default AWS owned KMS key is used."
    },
    "AdditionalEncryptionContext" : {
      "$ref" : "#/definitions/EncryptionContextMap"
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
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
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
    "/properties/KmsKeyId" : "$join([\"arn:(aws)[-]{0,1}[a-z]{0,2}[-]{0,1}[a-z]{0,3}:kms:[a-z]{2}[-]{1}[a-z]{3,10}[-]{0,1}[a-z]{0,10}[-]{1}[1-3]{1}:[0-9]{12}[:]{1}key\\/\", KmsKeyId])"
  },
  "createOnlyProperties" : [ "/properties/SourceArn", "/properties/TargetArn", "/properties/KMSKeyId", "/properties/AdditionalEncryptionContext" ],
  "readOnlyProperties" : [ "/properties/IntegrationArn", "/properties/CreateTime" ],
  "primaryIdentifier" : [ "/properties/IntegrationArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "redshift:CreateIntegration", "redshift:DescribeIntegrations", "redshift:CreateTags", "redshift:DescribeTags", "redshift:DescribeClusters", "redshift:CreateInboundIntegration", "redshift-serverless:ListNamespaces", "kms:CreateGrant", "kms:DescribeKey" ]
    },
    "read" : {
      "permissions" : [ "redshift:DescribeIntegrations", "redshift:DescribeTags" ]
    },
    "update" : {
      "permissions" : [ "redshift:DescribeIntegrations", "redshift:ModifyIntegration", "redshift:CreateTags", "redshift:DeleteTags", "redshift:DescribeClusters", "redshift:DescribeTags", "redshift-serverless:ListNamespaces" ]
    },
    "delete" : {
      "permissions" : [ "redshift:DeleteTags", "redshift:DeleteIntegration", "redshift:DescribeIntegrations" ]
    },
    "list" : {
      "permissions" : [ "redshift:DescribeTags", "redshift:DescribeIntegrations" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "redshift:CreateTags", "redshift:DeleteTags", "redshift:DescribeTags" ]
  },
  "additionalProperties" : False
}