SCHEMA = {
  "typeName" : "AWS::RDS::GlobalCluster",
  "description" : "Resource Type definition for AWS::RDS::GlobalCluster",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-rds",
  "properties" : {
    "Engine" : {
      "description" : "The name of the database engine to be used for this DB cluster. Valid Values: aurora (for MySQL 5.6-compatible Aurora), aurora-mysql (for MySQL 5.7-compatible Aurora).\nIf you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.",
      "type" : "string",
      "enum" : [ "aurora", "aurora-mysql", "aurora-postgresql" ]
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
    "EngineLifecycleSupport" : {
      "description" : "The life cycle type of the global cluster. You can use this setting to enroll your global cluster into Amazon RDS Extended Support.",
      "type" : "string"
    },
    "EngineVersion" : {
      "description" : "The version number of the database engine to use. If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.",
      "type" : "string"
    },
    "DeletionProtection" : {
      "description" : "The deletion protection setting for the new global database. The global database can't be deleted when deletion protection is enabled.",
      "type" : "boolean"
    },
    "GlobalClusterIdentifier" : {
      "description" : "The cluster identifier of the new global database cluster. This parameter is stored as a lowercase string.",
      "type" : "string",
      "pattern" : "^[a-zA-Z]{1}(?:-?[a-zA-Z0-9]){0,62}$",
      "minLength" : 1,
      "maxLength" : 63
    },
    "SourceDBClusterIdentifier" : {
      "description" : "The Amazon Resource Name (ARN) to use as the primary cluster of the global database. This parameter is optional. This parameter is stored as a lowercase string.",
      "type" : "string",
      "oneOf" : [ {
        "pattern" : "^[a-zA-Z]{1}(?:-?[a-zA-Z0-9]){0,62}$"
      }, {
        "pattern" : "^(?=.{40,128}$)arn.*"
      } ]
    },
    "StorageEncrypted" : {
      "description" : " The storage encryption setting for the new global database cluster.\nIf you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.",
      "type" : "boolean"
    },
    "GlobalEndpoint" : {
      "$ref" : "#/definitions/GlobalEndpoint"
    }
  },
  "definitions" : {
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
    "GlobalEndpoint" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Address" : {
          "description" : "The writer endpoint for the global database cluster. This endpoint always points to the writer DB instance in the current primary cluster.",
          "type" : "string"
        }
      }
    }
  },
  "oneOf" : [ {
    "required" : [ "SourceDBClusterIdentifier" ]
  }, {
    "required" : [ "Engine" ]
  } ],
  "additionalProperties" : False,
  "propertyTransform" : {
    "/properties/GlobalClusterIdentifier" : "$lowercase(GlobalClusterIdentifier)"
  },
  "readOnlyProperties" : [ "/properties/GlobalEndpoint" ],
  "createOnlyProperties" : [ "/properties/GlobalClusterIdentifier", "/properties/SourceDBClusterIdentifier", "/properties/StorageEncrypted", "/properties/Engine" ],
  "primaryIdentifier" : [ "/properties/GlobalClusterIdentifier" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "rds:CreateGlobalCluster", "rds:DescribeDBClusters", "rds:DescribeGlobalClusters" ]
    },
    "read" : {
      "permissions" : [ "rds:DescribeGlobalClusters" ]
    },
    "update" : {
      "permissions" : [ "rds:ModifyGlobalCluster", "rds:DescribeGlobalClusters", "rds:AddTagsToResource", "rds:RemoveTagsFromResource" ]
    },
    "delete" : {
      "permissions" : [ "rds:DescribeGlobalClusters", "rds:DeleteGlobalCluster", "rds:RemoveFromGlobalCluster", "rds:DescribeDBClusters" ]
    },
    "list" : {
      "permissions" : [ "rds:DescribeGlobalClusters" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "rds:AddTagsToResource", "rds:RemoveTagsFromResource" ]
  }
}