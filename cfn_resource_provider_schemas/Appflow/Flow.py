SCHEMA = {
  "typeName" : "AWS::AppFlow::Flow",
  "description" : "Resource schema for AWS::AppFlow::Flow.",
  "sourceUrl" : "https://docs.aws.amazon.com/appflow/latest/userguide/what-is-appflow.html",
  "additionalProperties" : False,
  "properties" : {
    "FlowArn" : {
      "description" : "ARN identifier of the flow.",
      "type" : "string",
      "pattern" : "arn:aws:appflow:.*:[0-9]+:.*",
      "maxLength" : 512
    },
    "FlowName" : {
      "description" : "Name of the flow.",
      "type" : "string",
      "pattern" : "[a-zA-Z0-9][\\w!@#.-]+",
      "maxLength" : 256,
      "minLength" : 1
    },
    "Description" : {
      "description" : "Description of the flow.",
      "type" : "string",
      "pattern" : "[\\w!@#\\-.?,\\s]*",
      "maxLength" : 2048
    },
    "KMSArn" : {
      "description" : "The ARN of the AWS Key Management Service (AWS KMS) key that's used to encrypt your function's environment variables. If it's not provided, AWS Lambda uses a default service key.",
      "type" : "string",
      "pattern" : "arn:aws:kms:.*:[0-9]+:.*",
      "maxLength" : 2048,
      "minLength" : 20
    },
    "TriggerConfig" : {
      "description" : "Trigger settings of the flow.",
      "$ref" : "#/definitions/TriggerConfig"
    },
    "FlowStatus" : {
      "description" : "Flow activation status for Scheduled- and Event-triggered flows",
      "type" : "string",
      "enum" : [ "Active", "Suspended", "Draft" ]
    },
    "SourceFlowConfig" : {
      "description" : "Configurations of Source connector of the flow.",
      "$ref" : "#/definitions/SourceFlowConfig"
    },
    "DestinationFlowConfigList" : {
      "description" : "List of Destination connectors of the flow.",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/DestinationFlowConfig"
      }
    },
    "Tasks" : {
      "description" : "List of tasks for the flow.",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Task"
      }
    },
    "Tags" : {
      "description" : "List of Tags.",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "MetadataCatalogConfig" : {
      "description" : "Configurations of metadata catalog of the flow.",
      "$ref" : "#/definitions/MetadataCatalogConfig"
    }
  },
  "definitions" : {
    "TriggerConfig" : {
      "description" : "Trigger settings of the flow.",
      "type" : "object",
      "properties" : {
        "TriggerType" : {
          "description" : "Trigger type of the flow",
          "$ref" : "#/definitions/TriggerType"
        },
        "TriggerProperties" : {
          "description" : "Details required based on the type of trigger",
          "$ref" : "#/definitions/ScheduledTriggerProperties"
        }
      },
      "required" : [ "TriggerType" ],
      "additionalProperties" : False
    },
    "SourceFlowConfig" : {
      "description" : "Configurations of Source connector of the flow.",
      "type" : "object",
      "properties" : {
        "ConnectorType" : {
          "description" : "Type of source connector",
          "$ref" : "#/definitions/ConnectorType"
        },
        "ApiVersion" : {
          "description" : "The API version that the destination connector uses.",
          "$ref" : "#/definitions/ApiVersion"
        },
        "ConnectorProfileName" : {
          "description" : "Name of source connector profile",
          "$ref" : "#/definitions/ConnectorProfileName"
        },
        "SourceConnectorProperties" : {
          "description" : "Source connector details required to query a connector",
          "$ref" : "#/definitions/SourceConnectorProperties"
        },
        "IncrementalPullConfig" : {
          "description" : "Configuration for scheduled incremental data pull",
          "$ref" : "#/definitions/IncrementalPullConfig"
        }
      },
      "required" : [ "ConnectorType", "SourceConnectorProperties" ],
      "additionalProperties" : False
    },
    "DestinationFlowConfig" : {
      "description" : "Configurations of destination connector.",
      "type" : "object",
      "properties" : {
        "ConnectorType" : {
          "description" : "Destination connector type",
          "$ref" : "#/definitions/ConnectorType"
        },
        "ApiVersion" : {
          "description" : "The API version that the destination connector uses.",
          "$ref" : "#/definitions/ApiVersion"
        },
        "ConnectorProfileName" : {
          "description" : "Name of destination connector profile",
          "$ref" : "#/definitions/ConnectorProfileName"
        },
        "DestinationConnectorProperties" : {
          "description" : "Destination connector details",
          "$ref" : "#/definitions/DestinationConnectorProperties"
        }
      },
      "required" : [ "ConnectorType", "DestinationConnectorProperties" ],
      "additionalProperties" : False
    },
    "Task" : {
      "type" : "object",
      "properties" : {
        "SourceFields" : {
          "description" : "Source fields on which particular task will be applied",
          "type" : "array",
          "items" : {
            "type" : "string"
          }
        },
        "ConnectorOperator" : {
          "description" : "Operation to be performed on provided source fields",
          "$ref" : "#/definitions/ConnectorOperator"
        },
        "DestinationField" : {
          "description" : "A field value on which source field should be validated",
          "type" : "string",
          "maxLength" : 256
        },
        "TaskType" : {
          "description" : "Type of task",
          "$ref" : "#/definitions/TaskType"
        },
        "TaskProperties" : {
          "description" : "A Map used to store task related info",
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/TaskPropertiesObject"
          }
        }
      },
      "required" : [ "SourceFields", "TaskType" ],
      "additionalProperties" : False
    },
    "Tag" : {
      "description" : "A label for tagging AppFlow resources",
      "type" : "object",
      "properties" : {
        "Key" : {
          "description" : "A string used to identify this tag",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "description" : "A string containing the value for the tag",
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    },
    "MetadataCatalogConfig" : {
      "description" : "Configurations of metadata catalog of the flow.",
      "type" : "object",
      "properties" : {
        "GlueDataCatalog" : {
          "description" : "Configurations of glue data catalog of the flow.",
          "$ref" : "#/definitions/GlueDataCatalog"
        }
      },
      "additionalProperties" : False
    },
    "GlueDataCatalog" : {
      "description" : "Trigger settings of the flow.",
      "type" : "object",
      "properties" : {
        "RoleArn" : {
          "description" : "A string containing the value for the tag",
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 512,
          "pattern" : "arn:aws:iam:.*:[0-9]+:.*"
        },
        "DatabaseName" : {
          "description" : "A string containing the value for the tag",
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 255,
          "pattern" : "[\\u0020-\\uD7FF\\uE000-\\uFFFD\\uD800\\uDC00-\\uDBFF\\uDFFF\\t]*"
        },
        "TablePrefix" : {
          "description" : "A string containing the value for the tag",
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 128,
          "pattern" : "[\\u0020-\\uD7FF\\uE000-\\uFFFD\\uD800\\uDC00-\\uDBFF\\uDFFF\\t]*"
        }
      },
      "required" : [ "RoleArn", "DatabaseName", "TablePrefix" ],
      "additionalProperties" : False
    },
    "DestinationConnectorProperties" : {
      "description" : "Destination connector details",
      "type" : "object",
      "properties" : {
        "Redshift" : {
          "$ref" : "#/definitions/RedshiftDestinationProperties"
        },
        "S3" : {
          "$ref" : "#/definitions/S3DestinationProperties"
        },
        "Salesforce" : {
          "$ref" : "#/definitions/SalesforceDestinationProperties"
        },
        "Snowflake" : {
          "$ref" : "#/definitions/SnowflakeDestinationProperties"
        },
        "EventBridge" : {
          "$ref" : "#/definitions/EventBridgeDestinationProperties"
        },
        "Upsolver" : {
          "$ref" : "#/definitions/UpsolverDestinationProperties"
        },
        "LookoutMetrics" : {
          "$ref" : "#/definitions/LookoutMetricsDestinationProperties"
        },
        "Marketo" : {
          "$ref" : "#/definitions/MarketoDestinationProperties"
        },
        "Zendesk" : {
          "$ref" : "#/definitions/ZendeskDestinationProperties"
        },
        "CustomConnector" : {
          "$ref" : "#/definitions/CustomConnectorDestinationProperties"
        },
        "SAPOData" : {
          "$ref" : "#/definitions/SAPODataDestinationProperties"
        }
      }
    },
    "IncrementalPullConfig" : {
      "description" : "Configuration for scheduled incremental data pull",
      "type" : "object",
      "properties" : {
        "DatetimeTypeFieldName" : {
          "$ref" : "#/definitions/DatetimeTypeFieldName"
        }
      }
    },
    "SourceConnectorProperties" : {
      "description" : "Source connector details required to query a connector",
      "type" : "object",
      "properties" : {
        "Amplitude" : {
          "$ref" : "#/definitions/AmplitudeSourceProperties"
        },
        "Datadog" : {
          "$ref" : "#/definitions/DatadogSourceProperties"
        },
        "Dynatrace" : {
          "$ref" : "#/definitions/DynatraceSourceProperties"
        },
        "GoogleAnalytics" : {
          "$ref" : "#/definitions/GoogleAnalyticsSourceProperties"
        },
        "InforNexus" : {
          "$ref" : "#/definitions/InforNexusSourceProperties"
        },
        "Marketo" : {
          "$ref" : "#/definitions/MarketoSourceProperties"
        },
        "S3" : {
          "$ref" : "#/definitions/S3SourceProperties"
        },
        "SAPOData" : {
          "$ref" : "#/definitions/SAPODataSourceProperties"
        },
        "Salesforce" : {
          "$ref" : "#/definitions/SalesforceSourceProperties"
        },
        "Pardot" : {
          "$ref" : "#/definitions/PardotSourceProperties"
        },
        "ServiceNow" : {
          "$ref" : "#/definitions/ServiceNowSourceProperties"
        },
        "Singular" : {
          "$ref" : "#/definitions/SingularSourceProperties"
        },
        "Slack" : {
          "$ref" : "#/definitions/SlackSourceProperties"
        },
        "Trendmicro" : {
          "$ref" : "#/definitions/TrendmicroSourceProperties"
        },
        "Veeva" : {
          "$ref" : "#/definitions/VeevaSourceProperties"
        },
        "Zendesk" : {
          "$ref" : "#/definitions/ZendeskSourceProperties"
        },
        "CustomConnector" : {
          "$ref" : "#/definitions/CustomConnectorSourceProperties"
        }
      }
    },
    "ConnectorOperator" : {
      "description" : "Operation to be performed on provided source fields",
      "type" : "object",
      "properties" : {
        "Amplitude" : {
          "$ref" : "#/definitions/AmplitudeConnectorOperator"
        },
        "Datadog" : {
          "$ref" : "#/definitions/DatadogConnectorOperator"
        },
        "Dynatrace" : {
          "$ref" : "#/definitions/DynatraceConnectorOperator"
        },
        "GoogleAnalytics" : {
          "$ref" : "#/definitions/GoogleAnalyticsConnectorOperator"
        },
        "InforNexus" : {
          "$ref" : "#/definitions/InforNexusConnectorOperator"
        },
        "Marketo" : {
          "$ref" : "#/definitions/MarketoConnectorOperator"
        },
        "S3" : {
          "$ref" : "#/definitions/S3ConnectorOperator"
        },
        "SAPOData" : {
          "$ref" : "#/definitions/SAPODataConnectorOperator"
        },
        "Salesforce" : {
          "$ref" : "#/definitions/SalesforceConnectorOperator"
        },
        "Pardot" : {
          "$ref" : "#/definitions/PardotConnectorOperator"
        },
        "ServiceNow" : {
          "$ref" : "#/definitions/ServiceNowConnectorOperator"
        },
        "Singular" : {
          "$ref" : "#/definitions/SingularConnectorOperator"
        },
        "Slack" : {
          "$ref" : "#/definitions/SlackConnectorOperator"
        },
        "Trendmicro" : {
          "$ref" : "#/definitions/TrendmicroConnectorOperator"
        },
        "Veeva" : {
          "$ref" : "#/definitions/VeevaConnectorOperator"
        },
        "Zendesk" : {
          "$ref" : "#/definitions/ZendeskConnectorOperator"
        },
        "CustomConnector" : {
          "$ref" : "#/definitions/Operator"
        }
      }
    },
    "ScheduledTriggerProperties" : {
      "description" : "Details required for scheduled trigger type",
      "type" : "object",
      "properties" : {
        "ScheduleExpression" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 256
        },
        "DataPullMode" : {
          "type" : "string",
          "enum" : [ "Incremental", "Complete" ]
        },
        "ScheduleStartTime" : {
          "type" : "number"
        },
        "ScheduleEndTime" : {
          "type" : "number"
        },
        "FirstExecutionFrom" : {
          "type" : "number"
        },
        "TimeZone" : {
          "type" : "string",
          "maxLength" : 256
        },
        "ScheduleOffset" : {
          "type" : "number",
          "minimum" : 0,
          "maximum" : 36000
        },
        "FlowErrorDeactivationThreshold" : {
          "type" : "integer",
          "minimum" : 1,
          "maximum" : 100
        }
      },
      "required" : [ "ScheduleExpression" ],
      "additionalProperties" : False
    },
    "CustomProperties" : {
      "description" : "A map for properties for custom connector.",
      "type" : "object",
      "patternProperties" : {
        "^[\\w]{1,2048}$" : {
          "description" : "A string containing the value for the property",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 2048,
          "pattern" : "\\S+"
        }
      },
      "required" : [ ],
      "additionalProperties" : False
    },
    "TriggerType" : {
      "type" : "string",
      "enum" : [ "Scheduled", "Event", "OnDemand" ]
    },
    "Object" : {
      "type" : "string",
      "maxLength" : 512,
      "pattern" : "\\S+"
    },
    "EntityName" : {
      "type" : "string",
      "maxLength" : 1024,
      "pattern" : "\\S+"
    },
    "EnableDynamicFieldUpdate" : {
      "type" : "boolean"
    },
    "IncludeDeletedRecords" : {
      "type" : "boolean"
    },
    "IncludeAllVersions" : {
      "type" : "boolean"
    },
    "IncludeRenditions" : {
      "type" : "boolean"
    },
    "IncludeSourceFiles" : {
      "type" : "boolean"
    },
    "DocumentType" : {
      "type" : "string",
      "maxLength" : 512,
      "pattern" : "[\\s\\w_-]+"
    },
    "BucketName" : {
      "type" : "string",
      "minLength" : 3,
      "maxLength" : 63,
      "pattern" : "\\S+"
    },
    "UpsolverBucketName" : {
      "type" : "string",
      "minLength" : 16,
      "maxLength" : 63,
      "pattern" : "^(upsolver-appflow)\\S*"
    },
    "BucketPrefix" : {
      "type" : "string",
      "maxLength" : 512
    },
    "S3InputFormatConfig" : {
      "type" : "object",
      "properties" : {
        "S3InputFileType" : {
          "type" : "string",
          "enum" : [ "CSV", "JSON" ]
        }
      }
    },
    "ErrorHandlingConfig" : {
      "type" : "object",
      "properties" : {
        "FailOnFirstError" : {
          "type" : "boolean"
        },
        "BucketPrefix" : {
          "$ref" : "#/definitions/BucketPrefix"
        },
        "BucketName" : {
          "$ref" : "#/definitions/BucketName"
        }
      },
      "additionalProperties" : False
    },
    "SuccessResponseHandlingConfig" : {
      "type" : "object",
      "properties" : {
        "BucketPrefix" : {
          "$ref" : "#/definitions/BucketPrefix"
        },
        "BucketName" : {
          "$ref" : "#/definitions/BucketName"
        }
      },
      "additionalProperties" : False
    },
    "Name" : {
      "type" : "string",
      "maxLength" : 128,
      "pattern" : "\\S+"
    },
    "WriteOperationType" : {
      "type" : "string",
      "enum" : [ "INSERT", "UPSERT", "UPDATE", "DELETE" ]
    },
    "FileType" : {
      "type" : "string",
      "enum" : [ "CSV", "JSON", "PARQUET" ]
    },
    "AggregationType" : {
      "type" : "string",
      "enum" : [ "None", "SingleFile" ]
    },
    "TargetFileSize" : {
      "type" : "integer"
    },
    "PreserveSourceDataTyping" : {
      "type" : "boolean"
    },
    "PrefixType" : {
      "type" : "string",
      "enum" : [ "FILENAME", "PATH", "PATH_AND_FILENAME" ]
    },
    "PrefixFormat" : {
      "type" : "string",
      "enum" : [ "YEAR", "MONTH", "DAY", "HOUR", "MINUTE" ]
    },
    "PathPrefixHierarchy" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/PathPrefix"
      }
    },
    "PathPrefix" : {
      "type" : "string",
      "enum" : [ "EXECUTION_ID", "SCHEMA_VERSION" ]
    },
    "PrefixConfig" : {
      "type" : "object",
      "properties" : {
        "PrefixType" : {
          "$ref" : "#/definitions/PrefixType"
        },
        "PrefixFormat" : {
          "$ref" : "#/definitions/PrefixFormat"
        },
        "PathPrefixHierarchy" : {
          "$ref" : "#/definitions/PathPrefixHierarchy"
        }
      },
      "additionalProperties" : False
    },
    "AggregationConfig" : {
      "type" : "object",
      "properties" : {
        "AggregationType" : {
          "$ref" : "#/definitions/AggregationType"
        },
        "TargetFileSize" : {
          "$ref" : "#/definitions/TargetFileSize"
        }
      }
    },
    "S3OutputFormatConfig" : {
      "type" : "object",
      "properties" : {
        "FileType" : {
          "$ref" : "#/definitions/FileType"
        },
        "PrefixConfig" : {
          "$ref" : "#/definitions/PrefixConfig"
        },
        "AggregationConfig" : {
          "$ref" : "#/definitions/AggregationConfig"
        },
        "PreserveSourceDataTyping" : {
          "$ref" : "#/definitions/PreserveSourceDataTyping"
        }
      },
      "additionalProperties" : False
    },
    "UpsolverS3OutputFormatConfig" : {
      "type" : "object",
      "properties" : {
        "FileType" : {
          "$ref" : "#/definitions/FileType"
        },
        "PrefixConfig" : {
          "$ref" : "#/definitions/PrefixConfig"
        },
        "AggregationConfig" : {
          "$ref" : "#/definitions/AggregationConfig"
        }
      },
      "required" : [ "PrefixConfig" ],
      "additionalProperties" : False
    },
    "ConnectorType" : {
      "type" : "string",
      "enum" : [ "SAPOData", "Salesforce", "Pardot", "Singular", "Slack", "Redshift", "S3", "Marketo", "Googleanalytics", "Zendesk", "Servicenow", "Datadog", "Trendmicro", "Snowflake", "Dynatrace", "Infornexus", "Amplitude", "Veeva", "CustomConnector", "EventBridge", "Upsolver", "LookoutMetrics" ]
    },
    "ApiVersion" : {
      "description" : "The API version that the connector will use.",
      "type" : "string",
      "pattern" : "\\S+",
      "maxLength" : 256
    },
    "ConnectorProfileName" : {
      "description" : "Name of connector profile",
      "type" : "string",
      "pattern" : "[\\w/!@#+=.-]+",
      "maxLength" : 256
    },
    "AmplitudeSourceProperties" : {
      "type" : "object",
      "properties" : {
        "Object" : {
          "$ref" : "#/definitions/Object"
        }
      },
      "required" : [ "Object" ],
      "additionalProperties" : False
    },
    "DatadogSourceProperties" : {
      "type" : "object",
      "properties" : {
        "Object" : {
          "$ref" : "#/definitions/Object"
        }
      },
      "required" : [ "Object" ],
      "additionalProperties" : False
    },
    "DynatraceSourceProperties" : {
      "type" : "object",
      "properties" : {
        "Object" : {
          "$ref" : "#/definitions/Object"
        }
      },
      "required" : [ "Object" ],
      "additionalProperties" : False
    },
    "GoogleAnalyticsSourceProperties" : {
      "type" : "object",
      "properties" : {
        "Object" : {
          "$ref" : "#/definitions/Object"
        }
      },
      "required" : [ "Object" ],
      "additionalProperties" : False
    },
    "InforNexusSourceProperties" : {
      "type" : "object",
      "properties" : {
        "Object" : {
          "$ref" : "#/definitions/Object"
        }
      },
      "required" : [ "Object" ],
      "additionalProperties" : False
    },
    "MarketoSourceProperties" : {
      "type" : "object",
      "properties" : {
        "Object" : {
          "$ref" : "#/definitions/Object"
        }
      },
      "required" : [ "Object" ],
      "additionalProperties" : False
    },
    "S3SourceProperties" : {
      "type" : "object",
      "properties" : {
        "BucketName" : {
          "$ref" : "#/definitions/BucketName"
        },
        "BucketPrefix" : {
          "$ref" : "#/definitions/BucketPrefix"
        },
        "S3InputFormatConfig" : {
          "$ref" : "#/definitions/S3InputFormatConfig"
        }
      },
      "required" : [ "BucketName", "BucketPrefix" ],
      "additionalProperties" : False
    },
    "SAPODataSourceProperties" : {
      "type" : "object",
      "properties" : {
        "ObjectPath" : {
          "$ref" : "#/definitions/Object"
        },
        "parallelismConfig" : {
          "$ref" : "#/definitions/SAPODataParallelismConfig"
        },
        "paginationConfig" : {
          "$ref" : "#/definitions/SAPODataPaginationConfig"
        }
      },
      "required" : [ "ObjectPath" ],
      "additionalProperties" : False
    },
    "SalesforceSourceProperties" : {
      "type" : "object",
      "properties" : {
        "Object" : {
          "$ref" : "#/definitions/Object"
        },
        "EnableDynamicFieldUpdate" : {
          "$ref" : "#/definitions/EnableDynamicFieldUpdate"
        },
        "IncludeDeletedRecords" : {
          "$ref" : "#/definitions/IncludeDeletedRecords"
        },
        "DataTransferApi" : {
          "$ref" : "#/definitions/DataTransferApi"
        }
      },
      "required" : [ "Object" ],
      "additionalProperties" : False
    },
    "PardotSourceProperties" : {
      "type" : "object",
      "properties" : {
        "Object" : {
          "$ref" : "#/definitions/Object"
        }
      },
      "required" : [ "Object" ],
      "additionalProperties" : False
    },
    "ServiceNowSourceProperties" : {
      "type" : "object",
      "properties" : {
        "Object" : {
          "$ref" : "#/definitions/Object"
        }
      },
      "required" : [ "Object" ],
      "additionalProperties" : False
    },
    "SingularSourceProperties" : {
      "type" : "object",
      "properties" : {
        "Object" : {
          "$ref" : "#/definitions/Object"
        }
      },
      "required" : [ "Object" ],
      "additionalProperties" : False
    },
    "SlackSourceProperties" : {
      "type" : "object",
      "properties" : {
        "Object" : {
          "$ref" : "#/definitions/Object"
        }
      },
      "required" : [ "Object" ],
      "additionalProperties" : False
    },
    "TrendmicroSourceProperties" : {
      "type" : "object",
      "properties" : {
        "Object" : {
          "$ref" : "#/definitions/Object"
        }
      },
      "required" : [ "Object" ],
      "additionalProperties" : False
    },
    "VeevaSourceProperties" : {
      "type" : "object",
      "properties" : {
        "Object" : {
          "$ref" : "#/definitions/Object"
        },
        "DocumentType" : {
          "$ref" : "#/definitions/DocumentType"
        },
        "IncludeSourceFiles" : {
          "$ref" : "#/definitions/IncludeSourceFiles"
        },
        "IncludeRenditions" : {
          "$ref" : "#/definitions/IncludeRenditions"
        },
        "IncludeAllVersions" : {
          "$ref" : "#/definitions/IncludeAllVersions"
        }
      },
      "required" : [ "Object" ],
      "additionalProperties" : False
    },
    "ZendeskSourceProperties" : {
      "type" : "object",
      "properties" : {
        "Object" : {
          "$ref" : "#/definitions/Object"
        }
      },
      "required" : [ "Object" ],
      "additionalProperties" : False
    },
    "CustomConnectorSourceProperties" : {
      "type" : "object",
      "properties" : {
        "EntityName" : {
          "$ref" : "#/definitions/EntityName"
        },
        "CustomProperties" : {
          "$ref" : "#/definitions/CustomProperties"
        },
        "DataTransferApi" : {
          "type" : "object",
          "properties" : {
            "Name" : {
              "type" : "string",
              "maxLength" : 64,
              "pattern" : "[\\w/-]+"
            },
            "Type" : {
              "type" : "string",
              "enum" : [ "SYNC", "ASYNC", "AUTOMATIC" ]
            }
          },
          "required" : [ "Name", "Type" ],
          "additionalProperties" : False
        }
      },
      "required" : [ "EntityName" ],
      "additionalProperties" : False
    },
    "CustomConnectorDestinationProperties" : {
      "type" : "object",
      "properties" : {
        "EntityName" : {
          "$ref" : "#/definitions/EntityName"
        },
        "ErrorHandlingConfig" : {
          "$ref" : "#/definitions/ErrorHandlingConfig"
        },
        "WriteOperationType" : {
          "$ref" : "#/definitions/WriteOperationType"
        },
        "IdFieldNames" : {
          "description" : "List of fields used as ID when performing a write operation.",
          "type" : "array",
          "items" : {
            "type" : "string"
          }
        },
        "CustomProperties" : {
          "$ref" : "#/definitions/CustomProperties"
        }
      },
      "required" : [ "EntityName" ],
      "additionalProperties" : False
    },
    "ZendeskDestinationProperties" : {
      "type" : "object",
      "properties" : {
        "Object" : {
          "$ref" : "#/definitions/Object"
        },
        "ErrorHandlingConfig" : {
          "$ref" : "#/definitions/ErrorHandlingConfig"
        },
        "IdFieldNames" : {
          "description" : "List of fields used as ID when performing a write operation.",
          "type" : "array",
          "items" : {
            "type" : "string"
          }
        },
        "WriteOperationType" : {
          "$ref" : "#/definitions/WriteOperationType"
        }
      },
      "required" : [ "Object" ],
      "additionalProperties" : False
    },
    "RedshiftDestinationProperties" : {
      "type" : "object",
      "properties" : {
        "Object" : {
          "$ref" : "#/definitions/Object"
        },
        "IntermediateBucketName" : {
          "$ref" : "#/definitions/BucketName"
        },
        "BucketPrefix" : {
          "$ref" : "#/definitions/BucketPrefix"
        },
        "ErrorHandlingConfig" : {
          "$ref" : "#/definitions/ErrorHandlingConfig"
        }
      },
      "required" : [ "Object", "IntermediateBucketName" ],
      "additionalProperties" : False
    },
    "S3DestinationProperties" : {
      "type" : "object",
      "properties" : {
        "BucketName" : {
          "$ref" : "#/definitions/BucketName"
        },
        "BucketPrefix" : {
          "$ref" : "#/definitions/BucketPrefix"
        },
        "S3OutputFormatConfig" : {
          "$ref" : "#/definitions/S3OutputFormatConfig"
        }
      },
      "required" : [ "BucketName" ],
      "additionalProperties" : False
    },
    "SAPODataDestinationProperties" : {
      "type" : "object",
      "properties" : {
        "ObjectPath" : {
          "$ref" : "#/definitions/Object"
        },
        "ErrorHandlingConfig" : {
          "$ref" : "#/definitions/ErrorHandlingConfig"
        },
        "SuccessResponseHandlingConfig" : {
          "$ref" : "#/definitions/SuccessResponseHandlingConfig"
        },
        "IdFieldNames" : {
          "description" : "List of fields used as ID when performing a write operation.",
          "type" : "array",
          "items" : {
            "type" : "string"
          }
        },
        "WriteOperationType" : {
          "$ref" : "#/definitions/WriteOperationType"
        }
      },
      "required" : [ "ObjectPath" ],
      "additionalProperties" : False
    },
    "SalesforceDestinationProperties" : {
      "type" : "object",
      "properties" : {
        "Object" : {
          "$ref" : "#/definitions/Object"
        },
        "ErrorHandlingConfig" : {
          "$ref" : "#/definitions/ErrorHandlingConfig"
        },
        "IdFieldNames" : {
          "description" : "List of fields used as ID when performing a write operation.",
          "type" : "array",
          "items" : {
            "type" : "string"
          }
        },
        "WriteOperationType" : {
          "$ref" : "#/definitions/WriteOperationType"
        },
        "DataTransferApi" : {
          "$ref" : "#/definitions/DataTransferApi"
        }
      },
      "required" : [ "Object" ],
      "additionalProperties" : False
    },
    "SnowflakeDestinationProperties" : {
      "type" : "object",
      "properties" : {
        "Object" : {
          "$ref" : "#/definitions/Object"
        },
        "IntermediateBucketName" : {
          "$ref" : "#/definitions/BucketName"
        },
        "BucketPrefix" : {
          "$ref" : "#/definitions/BucketPrefix"
        },
        "ErrorHandlingConfig" : {
          "$ref" : "#/definitions/ErrorHandlingConfig"
        }
      },
      "required" : [ "Object", "IntermediateBucketName" ],
      "additionalProperties" : False
    },
    "EventBridgeDestinationProperties" : {
      "type" : "object",
      "properties" : {
        "Object" : {
          "$ref" : "#/definitions/Object"
        },
        "ErrorHandlingConfig" : {
          "$ref" : "#/definitions/ErrorHandlingConfig"
        }
      },
      "required" : [ "Object" ],
      "additionalProperties" : False
    },
    "UpsolverDestinationProperties" : {
      "type" : "object",
      "properties" : {
        "BucketName" : {
          "$ref" : "#/definitions/UpsolverBucketName"
        },
        "BucketPrefix" : {
          "$ref" : "#/definitions/BucketPrefix"
        },
        "S3OutputFormatConfig" : {
          "$ref" : "#/definitions/UpsolverS3OutputFormatConfig"
        }
      },
      "required" : [ "BucketName", "S3OutputFormatConfig" ],
      "additionalProperties" : False
    },
    "LookoutMetricsDestinationProperties" : {
      "type" : "object",
      "properties" : {
        "Object" : {
          "$ref" : "#/definitions/Object"
        }
      },
      "additionalProperties" : False
    },
    "MarketoDestinationProperties" : {
      "type" : "object",
      "properties" : {
        "Object" : {
          "$ref" : "#/definitions/Object"
        },
        "ErrorHandlingConfig" : {
          "$ref" : "#/definitions/ErrorHandlingConfig"
        }
      },
      "required" : [ "Object" ],
      "additionalProperties" : False
    },
    "DatetimeTypeFieldName" : {
      "description" : "Name of the datetime/timestamp data type field to be used for importing incremental records from the source",
      "type" : "string",
      "maxLength" : 256
    },
    "TaskType" : {
      "type" : "string",
      "enum" : [ "Arithmetic", "Filter", "Map", "Map_all", "Mask", "Merge", "Passthrough", "Truncate", "Validate", "Partition" ]
    },
    "OperatorPropertiesKeys" : {
      "type" : "string",
      "enum" : [ "VALUE", "VALUES", "DATA_TYPE", "UPPER_BOUND", "LOWER_BOUND", "SOURCE_DATA_TYPE", "DESTINATION_DATA_TYPE", "VALIDATION_ACTION", "MASK_VALUE", "MASK_LENGTH", "TRUNCATE_LENGTH", "MATH_OPERATION_FIELDS_ORDER", "CONCAT_FORMAT", "SUBFIELD_CATEGORY_MAP", "EXCLUDE_SOURCE_FIELDS_LIST", "INCLUDE_NEW_FIELDS", "ORDERED_PARTITION_KEYS_LIST" ]
    },
    "TaskPropertiesObject" : {
      "description" : "An object used to store task related info",
      "type" : "object",
      "properties" : {
        "Key" : {
          "$ref" : "#/definitions/OperatorPropertiesKeys"
        },
        "Value" : {
          "type" : "string",
          "maxLength" : 2048,
          "pattern" : ".+"
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    },
    "AmplitudeConnectorOperator" : {
      "type" : "string",
      "enum" : [ "BETWEEN" ]
    },
    "DatadogConnectorOperator" : {
      "type" : "string",
      "enum" : [ "PROJECTION", "BETWEEN", "EQUAL_TO", "ADDITION", "MULTIPLICATION", "DIVISION", "SUBTRACTION", "MASK_ALL", "MASK_FIRST_N", "MASK_LAST_N", "VALIDATE_NON_NULL", "VALIDATE_NON_ZERO", "VALIDATE_NON_NEGATIVE", "VALIDATE_NUMERIC", "NO_OP" ]
    },
    "DynatraceConnectorOperator" : {
      "type" : "string",
      "enum" : [ "PROJECTION", "BETWEEN", "EQUAL_TO", "ADDITION", "MULTIPLICATION", "DIVISION", "SUBTRACTION", "MASK_ALL", "MASK_FIRST_N", "MASK_LAST_N", "VALIDATE_NON_NULL", "VALIDATE_NON_ZERO", "VALIDATE_NON_NEGATIVE", "VALIDATE_NUMERIC", "NO_OP" ]
    },
    "GoogleAnalyticsConnectorOperator" : {
      "type" : "string",
      "enum" : [ "PROJECTION", "BETWEEN" ]
    },
    "InforNexusConnectorOperator" : {
      "type" : "string",
      "enum" : [ "PROJECTION", "BETWEEN", "EQUAL_TO", "ADDITION", "MULTIPLICATION", "DIVISION", "SUBTRACTION", "MASK_ALL", "MASK_FIRST_N", "MASK_LAST_N", "VALIDATE_NON_NULL", "VALIDATE_NON_ZERO", "VALIDATE_NON_NEGATIVE", "VALIDATE_NUMERIC", "NO_OP" ]
    },
    "MarketoConnectorOperator" : {
      "type" : "string",
      "enum" : [ "PROJECTION", "LESS_THAN", "GREATER_THAN", "BETWEEN", "ADDITION", "MULTIPLICATION", "DIVISION", "SUBTRACTION", "MASK_ALL", "MASK_FIRST_N", "MASK_LAST_N", "VALIDATE_NON_NULL", "VALIDATE_NON_ZERO", "VALIDATE_NON_NEGATIVE", "VALIDATE_NUMERIC", "NO_OP" ]
    },
    "S3ConnectorOperator" : {
      "type" : "string",
      "enum" : [ "PROJECTION", "LESS_THAN", "GREATER_THAN", "BETWEEN", "LESS_THAN_OR_EQUAL_TO", "GREATER_THAN_OR_EQUAL_TO", "EQUAL_TO", "NOT_EQUAL_TO", "ADDITION", "MULTIPLICATION", "DIVISION", "SUBTRACTION", "MASK_ALL", "MASK_FIRST_N", "MASK_LAST_N", "VALIDATE_NON_NULL", "VALIDATE_NON_ZERO", "VALIDATE_NON_NEGATIVE", "VALIDATE_NUMERIC", "NO_OP" ]
    },
    "SAPODataConnectorOperator" : {
      "type" : "string",
      "enum" : [ "PROJECTION", "LESS_THAN", "CONTAINS", "GREATER_THAN", "BETWEEN", "LESS_THAN_OR_EQUAL_TO", "GREATER_THAN_OR_EQUAL_TO", "EQUAL_TO", "NOT_EQUAL_TO", "ADDITION", "MULTIPLICATION", "DIVISION", "SUBTRACTION", "MASK_ALL", "MASK_FIRST_N", "MASK_LAST_N", "VALIDATE_NON_NULL", "VALIDATE_NON_ZERO", "VALIDATE_NON_NEGATIVE", "VALIDATE_NUMERIC", "NO_OP" ]
    },
    "SalesforceConnectorOperator" : {
      "type" : "string",
      "enum" : [ "PROJECTION", "LESS_THAN", "CONTAINS", "GREATER_THAN", "BETWEEN", "LESS_THAN_OR_EQUAL_TO", "GREATER_THAN_OR_EQUAL_TO", "EQUAL_TO", "NOT_EQUAL_TO", "ADDITION", "MULTIPLICATION", "DIVISION", "SUBTRACTION", "MASK_ALL", "MASK_FIRST_N", "MASK_LAST_N", "VALIDATE_NON_NULL", "VALIDATE_NON_ZERO", "VALIDATE_NON_NEGATIVE", "VALIDATE_NUMERIC", "NO_OP" ]
    },
    "PardotConnectorOperator" : {
      "type" : "string",
      "enum" : [ "PROJECTION", "EQUAL_TO", "NO_OP", "ADDITION", "MULTIPLICATION", "DIVISION", "SUBTRACTION", "MASK_ALL", "MASK_FIRST_N", "MASK_LAST_N", "VALIDATE_NON_NULL", "VALIDATE_NON_ZERO", "VALIDATE_NON_NEGATIVE", "VALIDATE_NUMERIC" ]
    },
    "ServiceNowConnectorOperator" : {
      "type" : "string",
      "enum" : [ "PROJECTION", "LESS_THAN", "CONTAINS", "GREATER_THAN", "BETWEEN", "LESS_THAN_OR_EQUAL_TO", "GREATER_THAN_OR_EQUAL_TO", "EQUAL_TO", "NOT_EQUAL_TO", "ADDITION", "MULTIPLICATION", "DIVISION", "SUBTRACTION", "MASK_ALL", "MASK_FIRST_N", "MASK_LAST_N", "VALIDATE_NON_NULL", "VALIDATE_NON_ZERO", "VALIDATE_NON_NEGATIVE", "VALIDATE_NUMERIC", "NO_OP" ]
    },
    "SingularConnectorOperator" : {
      "type" : "string",
      "enum" : [ "PROJECTION", "EQUAL_TO", "ADDITION", "MULTIPLICATION", "DIVISION", "SUBTRACTION", "MASK_ALL", "MASK_FIRST_N", "MASK_LAST_N", "VALIDATE_NON_NULL", "VALIDATE_NON_ZERO", "VALIDATE_NON_NEGATIVE", "VALIDATE_NUMERIC", "NO_OP" ]
    },
    "SlackConnectorOperator" : {
      "type" : "string",
      "enum" : [ "PROJECTION", "BETWEEN", "EQUAL_TO", "ADDITION", "MULTIPLICATION", "DIVISION", "SUBTRACTION", "MASK_ALL", "MASK_FIRST_N", "MASK_LAST_N", "VALIDATE_NON_NULL", "VALIDATE_NON_ZERO", "VALIDATE_NON_NEGATIVE", "VALIDATE_NUMERIC", "NO_OP" ]
    },
    "TrendmicroConnectorOperator" : {
      "type" : "string",
      "enum" : [ "PROJECTION", "EQUAL_TO", "ADDITION", "MULTIPLICATION", "DIVISION", "SUBTRACTION", "MASK_ALL", "MASK_FIRST_N", "MASK_LAST_N", "VALIDATE_NON_NULL", "VALIDATE_NON_ZERO", "VALIDATE_NON_NEGATIVE", "VALIDATE_NUMERIC", "NO_OP" ]
    },
    "VeevaConnectorOperator" : {
      "type" : "string",
      "enum" : [ "PROJECTION", "LESS_THAN", "GREATER_THAN", "BETWEEN", "LESS_THAN_OR_EQUAL_TO", "GREATER_THAN_OR_EQUAL_TO", "EQUAL_TO", "NOT_EQUAL_TO", "ADDITION", "MULTIPLICATION", "DIVISION", "SUBTRACTION", "MASK_ALL", "MASK_FIRST_N", "MASK_LAST_N", "VALIDATE_NON_NULL", "VALIDATE_NON_ZERO", "VALIDATE_NON_NEGATIVE", "VALIDATE_NUMERIC", "NO_OP" ]
    },
    "ZendeskConnectorOperator" : {
      "type" : "string",
      "enum" : [ "PROJECTION", "GREATER_THAN", "ADDITION", "MULTIPLICATION", "DIVISION", "SUBTRACTION", "MASK_ALL", "MASK_FIRST_N", "MASK_LAST_N", "VALIDATE_NON_NULL", "VALIDATE_NON_ZERO", "VALIDATE_NON_NEGATIVE", "VALIDATE_NUMERIC", "NO_OP" ]
    },
    "Operator" : {
      "type" : "string",
      "enum" : [ "PROJECTION", "LESS_THAN", "GREATER_THAN", "CONTAINS", "BETWEEN", "LESS_THAN_OR_EQUAL_TO", "GREATER_THAN_OR_EQUAL_TO", "EQUAL_TO", "NOT_EQUAL_TO", "ADDITION", "MULTIPLICATION", "DIVISION", "SUBTRACTION", "MASK_ALL", "MASK_FIRST_N", "MASK_LAST_N", "VALIDATE_NON_NULL", "VALIDATE_NON_ZERO", "VALIDATE_NON_NEGATIVE", "VALIDATE_NUMERIC", "NO_OP" ]
    },
    "Status" : {
      "type" : "string",
      "enum" : [ "Active", "Draft", "Errored", "Suspended" ]
    },
    "DataTransferApi" : {
      "type" : "string",
      "enum" : [ "AUTOMATIC", "BULKV2", "REST_SYNC" ]
    },
    "SAPODataParallelismConfig" : {
      "description" : "SAP Source connector parallelism factor",
      "type" : "object",
      "properties" : {
        "maxParallelism" : {
          "$ref" : "#/definitions/SAPODataMaxParallelism"
        }
      },
      "required" : [ "maxParallelism" ],
      "additionalProperties" : False
    },
    "SAPODataPaginationConfig" : {
      "description" : "SAP Source connector page size",
      "type" : "object",
      "properties" : {
        "maxPageSize" : {
          "$ref" : "#/definitions/SAPODataMaxPageSize"
        }
      },
      "required" : [ "maxPageSize" ],
      "additionalProperties" : False
    },
    "SAPODataMaxParallelism" : {
      "type" : "integer",
      "minimum" : 1,
      "maximum" : 10
    },
    "SAPODataMaxPageSize" : {
      "type" : "integer",
      "minimum" : 1,
      "maximum" : 10000
    }
  },
  "required" : [ "FlowName", "Tasks", "SourceFlowConfig", "DestinationFlowConfigList", "TriggerConfig" ],
  "createOnlyProperties" : [ "/properties/FlowName", "/properties/KMSArn" ],
  "readOnlyProperties" : [ "/properties/FlowArn" ],
  "primaryIdentifier" : [ "/properties/FlowName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "appflow:CreateFlow", "appflow:StartFlow", "appflow:TagResource", "appflow:ListTagsForResource", "appflow:UseConnectorProfile", "iam:PassRole", "s3:ListAllMyBuckets", "s3:GetBucketLocation", "s3:GetBucketPolicy", "kms:ListGrants", "kms:ListKeys", "kms:DescribeKey", "kms:ListAliases", "kms:CreateGrant", "secretsmanager:CreateSecret", "secretsmanager:PutResourcePolicy" ]
    },
    "read" : {
      "permissions" : [ "appflow:DescribeFlow", "appflow:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "appflow:DescribeFlow", "appflow:UpdateFlow", "appflow:StartFlow", "appflow:StopFlow", "appflow:TagResource", "appflow:UntagResource", "appflow:ListTagsForResource", "appflow:UseConnectorProfile", "iam:PassRole", "s3:ListAllMyBuckets", "s3:GetBucketLocation", "s3:GetBucketPolicy", "kms:ListGrants", "secretsmanager:CreateSecret", "secretsmanager:PutResourcePolicy" ]
    },
    "delete" : {
      "permissions" : [ "appflow:DeleteFlow" ]
    },
    "list" : {
      "permissions" : [ "appflow:ListFlows" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "appflow:TagResource", "appflow:UntagResource", "appflow:ListTagsForResource" ]
  }
}