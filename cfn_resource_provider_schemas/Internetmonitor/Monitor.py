SCHEMA = {
  "typeName" : "AWS::InternetMonitor::Monitor",
  "description" : "Represents a monitor, which defines the monitoring boundaries for measurements that Internet Monitor publishes information about for an application",
  "definitions" : {
    "MonitorConfigState" : {
      "type" : "string",
      "enum" : [ "PENDING", "ACTIVE", "INACTIVE", "ERROR" ]
    },
    "MonitorProcessingStatusCode" : {
      "type" : "string",
      "enum" : [ "OK", "INACTIVE", "COLLECTING_DATA", "INSUFFICIENT_DATA", "FAULT_SERVICE", "FAULT_ACCESS_CLOUDWATCH" ]
    },
    "Tag" : {
      "description" : "The metadata that you apply to the cluster to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string"
        },
        "Value" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False
    },
    "iso8601UTC" : {
      "description" : "The date value in ISO 8601 format. The timezone is always UTC. (YYYY-MM-DDThh:mm:ssZ)",
      "type" : "string",
      "pattern" : "^([0-2]\\d{3})-(0[0-9]|1[0-2])-([0-2]\\d|3[01])T([01]\\d|2[0-4]):([0-5]\\d):([0-6]\\d)((\\.\\d{3})?)Z$"
    },
    "InternetMeasurementsLogDelivery" : {
      "type" : "object",
      "properties" : {
        "S3Config" : {
          "$ref" : "#/definitions/S3Config"
        }
      },
      "additionalProperties" : False
    },
    "S3Config" : {
      "type" : "object",
      "properties" : {
        "BucketName" : {
          "type" : "string",
          "minLength" : 3
        },
        "BucketPrefix" : {
          "type" : "string"
        },
        "LogDeliveryStatus" : {
          "type" : "string",
          "enum" : [ "ENABLED", "DISABLED" ]
        }
      },
      "additionalProperties" : False
    },
    "HealthEventsConfig" : {
      "type" : "object",
      "properties" : {
        "AvailabilityScoreThreshold" : {
          "type" : "number",
          "minimum" : 0.0,
          "maximum" : 100.0
        },
        "PerformanceScoreThreshold" : {
          "type" : "number",
          "minimum" : 0.0,
          "maximum" : 100.0
        },
        "AvailabilityLocalHealthEventsConfig" : {
          "$ref" : "#/definitions/LocalHealthEventsConfig"
        },
        "PerformanceLocalHealthEventsConfig" : {
          "$ref" : "#/definitions/LocalHealthEventsConfig"
        }
      },
      "additionalProperties" : False
    },
    "LocalHealthEventsConfig" : {
      "type" : "object",
      "properties" : {
        "Status" : {
          "type" : "string",
          "enum" : [ "ENABLED", "DISABLED" ]
        },
        "HealthScoreThreshold" : {
          "type" : "number",
          "minimum" : 0.0,
          "maximum" : 100.0
        },
        "MinTrafficImpact" : {
          "type" : "number",
          "minimum" : 0.0,
          "maximum" : 100.0
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "CreatedAt" : {
      "$ref" : "#/definitions/iso8601UTC"
    },
    "ModifiedAt" : {
      "$ref" : "#/definitions/iso8601UTC"
    },
    "MonitorArn" : {
      "type" : "string",
      "maxLength" : 512,
      "minLength" : 20,
      "pattern" : "^arn:.*"
    },
    "MonitorName" : {
      "type" : "string",
      "maxLength" : 255,
      "minLength" : 1,
      "pattern" : "^[a-zA-Z0-9_.-]+$"
    },
    "LinkedAccountId" : {
      "type" : "string",
      "maxLength" : 12,
      "minLength" : 12,
      "pattern" : "^(\\d{12})$"
    },
    "IncludeLinkedAccounts" : {
      "type" : "boolean"
    },
    "ProcessingStatus" : {
      "$ref" : "#/definitions/MonitorProcessingStatusCode"
    },
    "ProcessingStatusInfo" : {
      "type" : "string"
    },
    "Resources" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "type" : "string",
        "maxLength" : 2048,
        "minLength" : 20,
        "pattern" : "^arn:.*"
      }
    },
    "ResourcesToAdd" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "type" : "string",
        "maxLength" : 2048,
        "minLength" : 20
      }
    },
    "ResourcesToRemove" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "type" : "string",
        "maxLength" : 2048,
        "minLength" : 20
      }
    },
    "Status" : {
      "$ref" : "#/definitions/MonitorConfigState"
    },
    "Tags" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "MaxCityNetworksToMonitor" : {
      "type" : "integer",
      "minimum" : 1,
      "maximum" : 500000
    },
    "TrafficPercentageToMonitor" : {
      "type" : "integer",
      "minimum" : 1,
      "maximum" : 100
    },
    "InternetMeasurementsLogDelivery" : {
      "$ref" : "#/definitions/InternetMeasurementsLogDelivery"
    },
    "HealthEventsConfig" : {
      "$ref" : "#/definitions/HealthEventsConfig"
    }
  },
  "readOnlyProperties" : [ "/properties/CreatedAt", "/properties/ModifiedAt", "/properties/MonitorArn", "/properties/ProcessingStatus", "/properties/ProcessingStatusInfo" ],
  "writeOnlyProperties" : [ "/properties/ResourcesToAdd", "/properties/ResourcesToRemove", "/properties/LinkedAccountId", "/properties/IncludeLinkedAccounts" ],
  "createOnlyProperties" : [ "/properties/MonitorName" ],
  "primaryIdentifier" : [ "/properties/MonitorName" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : False,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "internetmonitor:TagResource", "internetmonitor:UntagResource", "internetmonitor:ListTagsForResource" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "internetmonitor:CreateMonitor", "internetmonitor:GetMonitor", "internetmonitor:TagResource", "internetmonitor:UntagResource", "logs:CreateLogDelivery", "logs:GetLogDelivery", "s3:GetBucketPolicy", "s3:PutBucketPolicy", "s3:ListBucket", "iam:PassRole" ]
    },
    "read" : {
      "permissions" : [ "internetmonitor:GetMonitor", "internetmonitor:ListTagsForResource", "logs:GetLogDelivery" ]
    },
    "update" : {
      "permissions" : [ "internetmonitor:CreateMonitor", "internetmonitor:GetMonitor", "internetmonitor:UpdateMonitor", "internetmonitor:TagResource", "internetmonitor:UntagResource", "logs:CreateLogDelivery", "logs:GetLogDelivery", "logs:UpdateLogDelivery", "logs:DeleteLogDelivery", "logs:ListLogDeliveries", "s3:GetBucketPolicy", "s3:PutBucketPolicy", "s3:ListBucket", "iam:PassRole" ]
    },
    "delete" : {
      "permissions" : [ "internetmonitor:UpdateMonitor", "internetmonitor:DeleteMonitor", "internetmonitor:GetMonitor", "logs:DeleteLogDelivery" ]
    },
    "list" : {
      "permissions" : [ "internetmonitor:ListMonitors", "internetmonitor:GetMonitor", "internetmonitor:ListTagsForResource", "logs:GetLogDelivery" ]
    }
  },
  "additionalProperties" : False,
  "required" : [ "MonitorName" ]
}