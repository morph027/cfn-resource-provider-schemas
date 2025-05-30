SCHEMA = {
  "typeName" : "AWS::DMS::DataMigration",
  "description" : "Resource schema for AWS::DMS::DataMigration.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "dms:AddTagsToResource", "dms:RemoveTagsFromResource", "dms:ListTagsForResource" ]
  },
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
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
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    },
    "DataMigrationSettings" : {
      "type" : "object",
      "properties" : {
        "CloudwatchLogsEnabled" : {
          "type" : "boolean",
          "description" : "The property specifies whether to enable the Cloudwatch log."
        },
        "NumberOfJobs" : {
          "type" : "integer",
          "description" : "The number of parallel jobs that trigger parallel threads to unload the tables from the source, and then load them to the target.",
          "minimum" : 1,
          "maximum" : 50
        },
        "SelectionRules" : {
          "type" : "string",
          "description" : "The property specifies the rules of selecting objects for data migration."
        }
      },
      "additionalProperties" : False
    },
    "SourceDataSettings" : {
      "type" : "object",
      "properties" : {
        "CDCStartPosition" : {
          "type" : "string",
          "description" : "The property is a point in the database engine's log that defines a time where you can begin CDC.",
          "maxLength" : 40
        },
        "CDCStartTime" : {
          "type" : "string",
          "description" : "The property indicates the start time for a change data capture (CDC) operation. The value is server time in UTC format.",
          "maxLength" : 40
        },
        "CDCStopTime" : {
          "type" : "string",
          "description" : "The property indicates the stop time for a change data capture (CDC) operation. The value is server time in UTC format.",
          "maxLength" : 40
        },
        "SlotName" : {
          "type" : "string",
          "description" : "The property sets the name of a previously created logical replication slot for a change data capture (CDC) load of the source instance.",
          "maxLength" : 255
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "DataMigrationName" : {
      "description" : "The property describes a name to identify the data migration.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 300
    },
    "DataMigrationArn" : {
      "description" : "The property describes an ARN of the data migration.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 300
    },
    "DataMigrationIdentifier" : {
      "description" : "The property describes an ARN of the data migration.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 300
    },
    "DataMigrationCreateTime" : {
      "description" : "The property describes the create time of the data migration.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 40
    },
    "ServiceAccessRoleArn" : {
      "description" : "The property describes Amazon Resource Name (ARN) of the service access role.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 300
    },
    "MigrationProjectIdentifier" : {
      "description" : "The property describes an identifier for the migration project. It is used for describing/deleting/modifying can be name/arn",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 255
    },
    "DataMigrationType" : {
      "description" : "The property describes the type of migration.",
      "type" : "string",
      "enum" : [ "full-load", "cdc", "full-load-and-cdc" ]
    },
    "DataMigrationSettings" : {
      "description" : "The property describes the settings for the data migration.",
      "$ref" : "#/definitions/DataMigrationSettings"
    },
    "SourceDataSettings" : {
      "description" : "The property describes the settings for the data migration.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/SourceDataSettings"
      }
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this resource.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "primaryIdentifier" : [ "/properties/DataMigrationArn" ],
  "additionalIdentifiers" : [ [ "/properties/DataMigrationName" ] ],
  "readOnlyProperties" : [ "/properties/DataMigrationArn", "/properties/DataMigrationCreateTime" ],
  "writeOnlyProperties" : [ "/properties/DataMigrationIdentifier" ],
  "required" : [ "DataMigrationType", "MigrationProjectIdentifier", "ServiceAccessRoleArn" ],
  "additionalProperties" : False,
  "handlers" : {
    "create" : {
      "permissions" : [ "dms:CreateDataMigration", "dms:DescribeDataMigrations", "dms:AddTagsToResource", "dms:ListTagsForResource", "iam:PassRole" ]
    },
    "read" : {
      "permissions" : [ "dms:DescribeDataMigrations", "dms:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "dms:ModifyDataMigration", "dms:AddTagsToResource", "dms:RemoveTagsFromResource", "dms:ListTagsForResource", "iam:PassRole" ]
    },
    "delete" : {
      "permissions" : [ "dms:DeleteDataMigration", "dms:RemoveTagsFromResource" ]
    },
    "list" : {
      "permissions" : [ "dms:DescribeDataMigrations", "dms:ListTagsForResource" ]
    }
  }
}