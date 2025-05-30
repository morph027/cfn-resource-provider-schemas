SCHEMA = {
  "typeName" : "AWS::CloudWatch::MetricStream",
  "description" : "Resource Type definition for Metric Stream",
  "additionalProperties" : False,
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-cloudwatch.git",
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "cloudwatch:TagResource", "cloudwatch:UntagResource", "cloudwatch:ListTagsForResource" ]
  },
  "properties" : {
    "Arn" : {
      "description" : "Amazon Resource Name of the metric stream.",
      "type" : "string",
      "minLength" : 20,
      "maxLength" : 2048
    },
    "CreationDate" : {
      "description" : "The date of creation of the metric stream.",
      "type" : "string",
      "anyOf" : [ {
        "format" : "date-time"
      }, {
        "format" : "timestamp"
      } ]
    },
    "ExcludeFilters" : {
      "description" : "Define which metrics will be not streamed. Metrics matched by multiple instances of MetricStreamFilter are joined with an OR operation by default. If both IncludeFilters and ExcludeFilters are omitted, all metrics in the account will be streamed. IncludeFilters and ExcludeFilters are mutually exclusive. Default to None.",
      "type" : "array",
      "maxItems" : 1000,
      "uniqueItems" : True,
      "items" : {
        "$ref" : "#/definitions/MetricStreamFilter"
      }
    },
    "FirehoseArn" : {
      "description" : "The ARN of the Kinesis Firehose where to stream the data.",
      "type" : "string",
      "minLength" : 20,
      "maxLength" : 2048
    },
    "IncludeFilters" : {
      "description" : "Define which metrics will be streamed. Metrics matched by multiple instances of MetricStreamFilter are joined with an OR operation by default. If both IncludeFilters and ExcludeFilters are omitted, all metrics in the account will be streamed. IncludeFilters and ExcludeFilters are mutually exclusive. Default to None.",
      "type" : "array",
      "maxItems" : 1000,
      "uniqueItems" : True,
      "items" : {
        "$ref" : "#/definitions/MetricStreamFilter"
      }
    },
    "LastUpdateDate" : {
      "description" : "The date of the last update of the metric stream.",
      "type" : "string",
      "anyOf" : [ {
        "format" : "date-time"
      }, {
        "format" : "timestamp"
      } ]
    },
    "Name" : {
      "description" : "Name of the metric stream.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 255
    },
    "RoleArn" : {
      "description" : "The ARN of the role that provides access to the Kinesis Firehose.",
      "type" : "string",
      "minLength" : 20,
      "maxLength" : 2048
    },
    "State" : {
      "description" : "Displays the state of the Metric Stream.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 255
    },
    "OutputFormat" : {
      "description" : "The output format of the data streamed to the Kinesis Firehose.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 255
    },
    "StatisticsConfigurations" : {
      "description" : "By default, a metric stream always sends the MAX, MIN, SUM, and SAMPLECOUNT statistics for each metric that is streamed. You can use this parameter to have the metric stream also send additional statistics in the stream. This array can have up to 100 members.",
      "type" : "array",
      "maxItems" : 100,
      "uniqueItems" : True,
      "items" : {
        "$ref" : "#/definitions/MetricStreamStatisticsConfiguration"
      }
    },
    "Tags" : {
      "description" : "A set of tags to assign to the delivery stream.",
      "type" : "array",
      "maxItems" : 50,
      "uniqueItems" : True,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "IncludeLinkedAccountsMetrics" : {
      "description" : "If you are creating a metric stream in a monitoring account, specify True to include metrics from source accounts that are linked to this monitoring account, in the metric stream. The default is False.",
      "type" : "boolean"
    }
  },
  "definitions" : {
    "MetricStreamFilter" : {
      "description" : "This structure defines the metrics that will be streamed.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Namespace" : {
          "description" : "Only metrics with Namespace matching this value will be streamed.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 255
        },
        "MetricNames" : {
          "description" : "Only metrics with MetricNames matching these values will be streamed. Must be set together with Namespace.",
          "type" : "array",
          "maxItems" : 999,
          "items" : {
            "type" : "string",
            "minLength" : 1,
            "maxLength" : 255
          }
        }
      },
      "required" : [ "Namespace" ]
    },
    "MetricStreamStatisticsConfiguration" : {
      "description" : "This structure specifies a list of additional statistics to stream, and the metrics to stream those additional statistics for. All metrics that match the combination of metric name and namespace will be streamed with the extended statistics, no matter their dimensions.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "AdditionalStatistics" : {
          "description" : "The additional statistics to stream for the metrics listed in IncludeMetrics.",
          "type" : "array",
          "maxItems" : 20,
          "uniqueItems" : True,
          "items" : {
            "type" : "string"
          }
        },
        "IncludeMetrics" : {
          "description" : "An array that defines the metrics that are to have additional statistics streamed.",
          "type" : "array",
          "maxItems" : 100,
          "uniqueItems" : True,
          "items" : {
            "$ref" : "#/definitions/MetricStreamStatisticsMetric"
          }
        }
      },
      "required" : [ "AdditionalStatistics", "IncludeMetrics" ]
    },
    "MetricStreamStatisticsMetric" : {
      "description" : "A structure that specifies the metric name and namespace for one metric that is going to have additional statistics included in the stream.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "MetricName" : {
          "description" : "The name of the metric.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 255
        },
        "Namespace" : {
          "description" : "The namespace of the metric.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 255
        }
      },
      "required" : [ "MetricName", "Namespace" ]
    },
    "Tag" : {
      "description" : "Metadata that you can assign to a Metric Stream, consisting of a key-value pair.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "description" : "A unique identifier for the tag.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "description" : "String which you can use to describe or define the tag.",
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ]
    }
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "cloudwatch:PutMetricStream", "cloudwatch:GetMetricStream", "cloudwatch:TagResource", "iam:PassRole" ]
    },
    "update" : {
      "permissions" : [ "cloudwatch:PutMetricStream", "cloudwatch:GetMetricStream", "cloudwatch:TagResource", "cloudwatch:UntagResource", "iam:PassRole" ]
    },
    "delete" : {
      "permissions" : [ "cloudwatch:DeleteMetricStream", "cloudwatch:GetMetricStream" ]
    },
    "list" : {
      "permissions" : [ "cloudwatch:ListMetricStreams" ]
    },
    "read" : {
      "permissions" : [ "cloudwatch:GetMetricStream", "cloudwatch:ListTagsForResource" ]
    }
  },
  "allOf" : [ {
    "required" : [ "FirehoseArn", "RoleArn", "OutputFormat" ]
  }, {
    "oneOf" : [ { }, {
      "required" : [ "IncludeFilters", "ExcludeFilters" ]
    } ]
  } ],
  "createOnlyProperties" : [ "/properties/Name" ],
  "primaryIdentifier" : [ "/properties/Name" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/CreationDate", "/properties/LastUpdateDate", "/properties/State" ]
}