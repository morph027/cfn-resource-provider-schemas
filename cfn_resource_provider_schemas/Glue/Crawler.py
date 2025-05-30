SCHEMA = {
  "typeName" : "AWS::Glue::Crawler",
  "description" : "Resource Type definition for AWS::Glue::Crawler",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-glue.git",
  "additionalProperties" : False,
  "properties" : {
    "Classifiers" : {
      "type" : "array",
      "description" : "A list of UTF-8 strings that specify the names of custom classifiers that are associated with the crawler.",
      "uniqueItems" : False,
      "items" : {
        "type" : "string"
      }
    },
    "Description" : {
      "type" : "string",
      "description" : "A description of the crawler."
    },
    "SchemaChangePolicy" : {
      "$ref" : "#/definitions/SchemaChangePolicy"
    },
    "Configuration" : {
      "type" : "string",
      "description" : "Crawler configuration information. This versioned JSON string allows users to specify aspects of a crawler's behavior."
    },
    "RecrawlPolicy" : {
      "$ref" : "#/definitions/RecrawlPolicy"
    },
    "DatabaseName" : {
      "type" : "string",
      "description" : "The name of the database in which the crawler's output is stored."
    },
    "Targets" : {
      "$ref" : "#/definitions/Targets"
    },
    "CrawlerSecurityConfiguration" : {
      "type" : "string",
      "description" : "The name of the SecurityConfiguration structure to be used by this crawler."
    },
    "Name" : {
      "type" : "string",
      "description" : "The name of the crawler."
    },
    "Role" : {
      "type" : "string",
      "description" : "The Amazon Resource Name (ARN) of an IAM role that's used to access customer resources, such as Amazon Simple Storage Service (Amazon S3) data."
    },
    "LakeFormationConfiguration" : {
      "$ref" : "#/definitions/LakeFormationConfiguration"
    },
    "Schedule" : {
      "$ref" : "#/definitions/Schedule"
    },
    "TablePrefix" : {
      "type" : "string",
      "description" : "The prefix added to the names of tables that are created."
    },
    "Tags" : {
      "type" : "object",
      "description" : "The tags to use with this crawler."
    }
  },
  "definitions" : {
    "S3Target" : {
      "type" : "object",
      "description" : "Specifies a data store in Amazon Simple Storage Service (Amazon S3).",
      "additionalProperties" : False,
      "properties" : {
        "ConnectionName" : {
          "type" : "string",
          "description" : "The name of a connection which allows a job or crawler to access data in Amazon S3 within an Amazon Virtual Private Cloud environment (Amazon VPC)."
        },
        "Path" : {
          "type" : "string",
          "description" : "The path to the Amazon S3 target."
        },
        "SampleSize" : {
          "type" : "integer",
          "description" : "Sets the number of files in each leaf folder to be crawled when crawling sample files in a dataset. If not set, all the files are crawled. A valid value is an integer between 1 and 249."
        },
        "Exclusions" : {
          "type" : "array",
          "description" : "A list of glob patterns used to exclude from the crawl.",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "DlqEventQueueArn" : {
          "type" : "string",
          "description" : "A valid Amazon dead-letter SQS ARN. For example, arn:aws:sqs:region:account:deadLetterQueue."
        },
        "EventQueueArn" : {
          "type" : "string",
          "description" : "A valid Amazon SQS ARN. For example, arn:aws:sqs:region:account:sqs."
        }
      }
    },
    "LakeFormationConfiguration" : {
      "type" : "object",
      "description" : "Specifies AWS Lake Formation configuration settings for the crawler",
      "additionalProperties" : False,
      "properties" : {
        "UseLakeFormationCredentials" : {
          "type" : "boolean",
          "description" : "Specifies whether to use AWS Lake Formation credentials for the crawler instead of the IAM role credentials."
        },
        "AccountId" : {
          "type" : "string",
          "description" : "Required for cross account crawls. For same account crawls as the target data, this can be left as None."
        }
      }
    },
    "SchemaChangePolicy" : {
      "type" : "object",
      "description" : "The policy that specifies update and delete behaviors for the crawler. The policy tells the crawler what to do in the event that it detects a change in a table that already exists in the customer's database at the time of the crawl. The SchemaChangePolicy does not affect whether or how new tables and partitions are added. New tables and partitions are always created regardless of the SchemaChangePolicy on a crawler. The SchemaChangePolicy consists of two components, UpdateBehavior and DeleteBehavior.",
      "additionalProperties" : False,
      "properties" : {
        "UpdateBehavior" : {
          "type" : "string",
          "description" : "The update behavior when the crawler finds a changed schema. A value of LOG specifies that if a table or a partition already exists, and a change is detected, do not update it, only log that a change was detected. Add new tables and new partitions (including on existing tables). A value of UPDATE_IN_DATABASE specifies that if a table or partition already exists, and a change is detected, update it. Add new tables and partitions."
        },
        "DeleteBehavior" : {
          "type" : "string",
          "description" : "The deletion behavior when the crawler finds a deleted object. A value of LOG specifies that if a table or partition is found to no longer exist, do not delete it, only log that it was found to no longer exist. A value of DELETE_FROM_DATABASE specifies that if a table or partition is found to have been removed, delete it from the database. A value of DEPRECATE_IN_DATABASE specifies that if a table has been found to no longer exist, to add a property to the table that says 'DEPRECATED' and includes a timestamp with the time of deprecation."
        }
      }
    },
    "IcebergTarget" : {
      "type" : "object",
      "description" : "Specifies Apache Iceberg data store targets.",
      "additionalProperties" : False,
      "properties" : {
        "ConnectionName" : {
          "type" : "string",
          "description" : "The name of the connection to use to connect to the Iceberg target."
        },
        "Paths" : {
          "type" : "array",
          "description" : "One or more Amazon S3 paths that contains Iceberg metadata folders as s3://bucket/prefix .",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "Exclusions" : {
          "type" : "array",
          "description" : "A list of global patterns used to exclude from the crawl.",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "MaximumTraversalDepth" : {
          "type" : "integer",
          "description" : "The maximum depth of Amazon S3 paths that the crawler can traverse to discover the Iceberg metadata folder in your Amazon S3 path. Used to limit the crawler run time."
        }
      }
    },
    "HudiTarget" : {
      "type" : "object",
      "description" : "Specifies Apache Hudi data store targets.",
      "additionalProperties" : False,
      "properties" : {
        "ConnectionName" : {
          "type" : "string",
          "description" : "The name of the connection to use to connect to the Hudi target."
        },
        "Paths" : {
          "type" : "array",
          "description" : "One or more Amazon S3 paths that contains Hudi metadata folders as s3://bucket/prefix .",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "Exclusions" : {
          "type" : "array",
          "description" : "A list of global patterns used to exclude from the crawl.",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "MaximumTraversalDepth" : {
          "type" : "integer",
          "description" : "The maximum depth of Amazon S3 paths that the crawler can traverse to discover the Hudi metadata folder in your Amazon S3 path. Used to limit the crawler run time."
        }
      }
    },
    "Schedule" : {
      "type" : "object",
      "description" : "A scheduling object using a cron statement to schedule an event.",
      "additionalProperties" : False,
      "properties" : {
        "ScheduleExpression" : {
          "type" : "string",
          "description" : "A cron expression used to specify the schedule. For more information, see Time-Based Schedules for Jobs and Crawlers. For example, to run something every day at 12:15 UTC, specify cron(15 12 * * ? *)."
        }
      }
    },
    "RecrawlPolicy" : {
      "type" : "object",
      "description" : "When crawling an Amazon S3 data source after the first crawl is complete, specifies whether to crawl the entire dataset again or to crawl only folders that were added since the last crawler run. For more information, see Incremental Crawls in AWS Glue in the developer guide.",
      "additionalProperties" : False,
      "properties" : {
        "RecrawlBehavior" : {
          "type" : "string",
          "description" : "Specifies whether to crawl the entire dataset again or to crawl only folders that were added since the last crawler run. A value of CRAWL_EVERYTHING specifies crawling the entire dataset again. A value of CRAWL_NEW_FOLDERS_ONLY specifies crawling only folders that were added since the last crawler run. A value of CRAWL_EVENT_MODE specifies crawling only the changes identified by Amazon S3 events."
        }
      }
    },
    "MongoDBTarget" : {
      "type" : "object",
      "description" : "Specifies an Amazon DocumentDB or MongoDB data store to crawl.",
      "additionalProperties" : False,
      "properties" : {
        "ConnectionName" : {
          "type" : "string",
          "description" : "The name of the connection to use to connect to the Amazon DocumentDB or MongoDB target."
        },
        "Path" : {
          "type" : "string",
          "description" : "The path of the Amazon DocumentDB or MongoDB target (database/collection)."
        }
      }
    },
    "DeltaTarget" : {
      "type" : "object",
      "description" : "Specifies a Delta data store to crawl one or more Delta tables.",
      "additionalProperties" : False,
      "properties" : {
        "ConnectionName" : {
          "type" : "string",
          "description" : "The name of the connection to use to connect to the Delta table target."
        },
        "CreateNativeDeltaTable" : {
          "type" : "boolean",
          "description" : "Specifies whether the crawler will create native tables, to allow integration with query engines that support querying of the Delta transaction log directly."
        },
        "WriteManifest" : {
          "type" : "boolean",
          "description" : "Specifies whether to write the manifest files to the Delta table path."
        },
        "DeltaTables" : {
          "type" : "array",
          "description" : "",
          "uniqueItems" : False,
          "items" : {
            "type" : "string",
            "description" : "A list of the Amazon S3 paths to the Delta tables."
          }
        }
      }
    },
    "JdbcTarget" : {
      "type" : "object",
      "description" : "Specifies a JDBC data store to crawl.",
      "additionalProperties" : False,
      "properties" : {
        "ConnectionName" : {
          "type" : "string",
          "description" : "The name of the connection to use to connect to the JDBC target."
        },
        "Path" : {
          "type" : "string",
          "description" : "The path of the JDBC target."
        },
        "Exclusions" : {
          "type" : "array",
          "description" : "A list of glob patterns used to exclude from the crawl. For more information, see Catalog Tables with a Crawler.",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "EnableAdditionalMetadata" : {
          "type" : "array",
          "description" : "Specify a value of RAWTYPES or COMMENTS to enable additional metadata in table responses. RAWTYPES provides the native-level datatype. COMMENTS provides comments associated with a column or table in the database.\n\nIf you do not need additional metadata, keep the field empty.",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        }
      }
    },
    "Targets" : {
      "type" : "object",
      "description" : "Specifies data stores to crawl.",
      "additionalProperties" : False,
      "properties" : {
        "S3Targets" : {
          "type" : "array",
          "description" : "Specifies Amazon Simple Storage Service (Amazon S3) targets.",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/S3Target"
          }
        },
        "CatalogTargets" : {
          "type" : "array",
          "description" : "Specifies AWS Glue Data Catalog targets.",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/CatalogTarget"
          }
        },
        "DeltaTargets" : {
          "type" : "array",
          "description" : "Specifies an array of Delta data store targets.",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/DeltaTarget"
          }
        },
        "MongoDBTargets" : {
          "type" : "array",
          "description" : "A list of Mongo DB targets.",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/MongoDBTarget"
          }
        },
        "JdbcTargets" : {
          "type" : "array",
          "description" : "Specifies JDBC targets.",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/JdbcTarget"
          }
        },
        "DynamoDBTargets" : {
          "type" : "array",
          "description" : "Specifies Amazon DynamoDB targets.",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/DynamoDBTarget"
          }
        },
        "IcebergTargets" : {
          "type" : "array",
          "description" : "Specifies Apache Iceberg data store targets.",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/IcebergTarget"
          }
        },
        "HudiTargets" : {
          "type" : "array",
          "description" : "Specifies Apache Hudi data store targets.",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/HudiTarget"
          }
        }
      }
    },
    "DynamoDBTarget" : {
      "type" : "object",
      "description" : "Specifies an Amazon DynamoDB table to crawl.",
      "additionalProperties" : False,
      "properties" : {
        "Path" : {
          "type" : "string",
          "description" : "The name of the DynamoDB table to crawl."
        }
      }
    },
    "CatalogTarget" : {
      "type" : "object",
      "description" : "Specifies an AWS Glue Data Catalog target.",
      "additionalProperties" : False,
      "properties" : {
        "ConnectionName" : {
          "type" : "string",
          "description" : "The name of the connection for an Amazon S3-backed Data Catalog table to be a target of the crawl when using a Catalog connection type paired with a NETWORK Connection type."
        },
        "DatabaseName" : {
          "type" : "string",
          "description" : "The name of the database to be synchronized."
        },
        "DlqEventQueueArn" : {
          "type" : "string",
          "description" : "A valid Amazon dead-letter SQS ARN. For example, arn:aws:sqs:region:account:deadLetterQueue."
        },
        "Tables" : {
          "type" : "array",
          "description" : "A list of the tables to be synchronized.",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "EventQueueArn" : {
          "type" : "string",
          "description" : "A valid Amazon SQS ARN. For example, arn:aws:sqs:region:account:sqs."
        }
      }
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "glue:TagResource", "glue:UntagResource" ]
  },
  "required" : [ "Role", "Targets" ],
  "createOnlyProperties" : [ "/properties/Name" ],
  "primaryIdentifier" : [ "/properties/Name" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "glue:CreateCrawler", "glue:GetCrawler", "glue:TagResource", "iam:PassRole" ]
    },
    "read" : {
      "permissions" : [ "glue:GetCrawler", "glue:GetTags", "iam:PassRole" ]
    },
    "update" : {
      "permissions" : [ "glue:UpdateCrawler", "glue:UntagResource", "glue:TagResource", "iam:PassRole" ]
    },
    "delete" : {
      "permissions" : [ "glue:DeleteCrawler", "glue:GetCrawler", "glue:StopCrawler", "iam:PassRole" ]
    },
    "list" : {
      "permissions" : [ "glue:ListCrawlers", "iam:PassRole" ]
    }
  }
}