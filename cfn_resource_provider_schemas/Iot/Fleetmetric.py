SCHEMA = {
  "typeName" : "AWS::IoT::FleetMetric",
  "description" : "An aggregated metric of certain devices in your fleet",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-iot.git",
  "taggable" : True,
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The tag's key",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The tag's value",
          "minLength" : 1,
          "maxLength" : 256
        }
      },
      "required" : [ "Value", "Key" ],
      "additionalProperties" : False
    },
    "AggregationType" : {
      "description" : "Aggregation types supported by Fleet Indexing",
      "type" : "object",
      "properties" : {
        "Name" : {
          "description" : "Fleet Indexing aggregation type names such as Statistics, Percentiles and Cardinality",
          "type" : "string"
        },
        "Values" : {
          "description" : "Fleet Indexing aggregation type values",
          "type" : "array",
          "insertionOrder" : False,
          "items" : {
            "type" : "string"
          }
        }
      },
      "required" : [ "Name", "Values" ],
      "additionalProperties" : False
    },
    "iso8601UTC" : {
      "description" : "The datetime value in ISO 8601 format. The timezone is always UTC. (YYYY-MM-DDThh:mm:ss.sssZ)",
      "type" : "string",
      "pattern" : "^([0-2]\\d{3})-(0[0-9]|1[0-2])-([0-2]\\d|3[01])T([01]\\d|2[0-4]):([0-5]\\d):([0-6]\\d)((\\.\\d{3})?)Z$"
    }
  },
  "properties" : {
    "MetricName" : {
      "description" : "The name of the fleet metric",
      "type" : "string"
    },
    "Description" : {
      "description" : "The description of a fleet metric",
      "type" : "string"
    },
    "QueryString" : {
      "description" : "The Fleet Indexing query used by a fleet metric",
      "type" : "string"
    },
    "Period" : {
      "description" : "The period of metric emission in seconds",
      "type" : "integer"
    },
    "AggregationField" : {
      "description" : "The aggregation field to perform aggregation and metric emission",
      "type" : "string"
    },
    "QueryVersion" : {
      "description" : "The version of a Fleet Indexing query used by a fleet metric",
      "type" : "string"
    },
    "IndexName" : {
      "description" : "The index name of a fleet metric",
      "type" : "string"
    },
    "Unit" : {
      "description" : "The unit of data points emitted by a fleet metric",
      "type" : "string"
    },
    "AggregationType" : {
      "$ref" : "#/definitions/AggregationType"
    },
    "MetricArn" : {
      "description" : "The Amazon Resource Number (ARN) of a fleet metric metric",
      "type" : "string"
    },
    "CreationDate" : {
      "description" : "The creation date of a fleet metric",
      "$ref" : "#/definitions/iso8601UTC"
    },
    "LastModifiedDate" : {
      "description" : "The last modified date of a fleet metric",
      "$ref" : "#/definitions/iso8601UTC"
    },
    "Version" : {
      "description" : "The version of a fleet metric",
      "type" : "number"
    },
    "Tags" : {
      "type" : "array",
      "maxItems" : 50,
      "uniqueItems" : True,
      "insertionOrder" : False,
      "description" : "An array of key-value pairs to apply to this resource",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "additionalProperties" : False,
  "required" : [ "MetricName" ],
  "readOnlyProperties" : [ "/properties/MetricArn", "/properties/CreationDate", "/properties/LastModifiedDate", "/properties/Version" ],
  "createOnlyProperties" : [ "/properties/MetricName" ],
  "primaryIdentifier" : [ "/properties/MetricName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iot:CreateFleetMetric", "iot:DescribeFleetMetric", "iot:TagResource" ]
    },
    "read" : {
      "permissions" : [ "iot:DescribeFleetMetric", "iot:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "iot:UpdateFleetMetric", "iot:DescribeFleetMetric", "iot:ListTagsForResource", "iot:UntagResource", "iot:TagResource" ]
    },
    "delete" : {
      "permissions" : [ "iot:DeleteFleetMetric", "iot:DescribeFleetMetric" ]
    },
    "list" : {
      "permissions" : [ "iot:ListFleetMetrics" ]
    }
  }
}