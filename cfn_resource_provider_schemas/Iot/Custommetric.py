SCHEMA = {
  "typeName" : "AWS::IoT::CustomMetric",
  "description" : "A custom metric published by your devices to Device Defender.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-iot.git",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The tag's key.",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The tag's value.",
          "minLength" : 1,
          "maxLength" : 256
        }
      },
      "required" : [ "Value", "Key" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "MetricName" : {
      "description" : "The name of the custom metric. This will be used in the metric report submitted from the device/thing. Shouldn't begin with aws: . Cannot be updated once defined.",
      "type" : "string",
      "pattern" : "[a-zA-Z0-9:_-]+",
      "minLength" : 1,
      "maxLength" : 128
    },
    "DisplayName" : {
      "description" : "Field represents a friendly name in the console for the custom metric; it doesn't have to be unique. Don't use this name as the metric identifier in the device metric report. Can be updated once defined.",
      "type" : "string",
      "maxLength" : 128
    },
    "MetricType" : {
      "description" : "The type of the custom metric. Types include string-list, ip-address-list, number-list, and number.",
      "type" : "string",
      "enum" : [ "string-list", "ip-address-list", "number-list", "number" ]
    },
    "MetricArn" : {
      "description" : "The Amazon Resource Number (ARN) of the custom metric.",
      "type" : "string",
      "minLength" : 20,
      "maxLength" : 2048
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
    }
  },
  "additionalProperties" : False,
  "required" : [ "MetricType" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "iot:TagResource", "iot:UntagResource", "iot:ListTagsForResource" ]
  },
  "createOnlyProperties" : [ "/properties/MetricName", "/properties/MetricType" ],
  "readOnlyProperties" : [ "/properties/MetricArn" ],
  "primaryIdentifier" : [ "/properties/MetricName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iot:CreateCustomMetric", "iot:TagResource" ]
    },
    "read" : {
      "permissions" : [ "iot:DescribeCustomMetric", "iot:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "iot:UpdateCustomMetric", "iot:ListTagsForResource", "iot:UntagResource", "iot:TagResource" ]
    },
    "delete" : {
      "permissions" : [ "iot:DescribeCustomMetric", "iot:DeleteCustomMetric" ]
    },
    "list" : {
      "permissions" : [ "iot:ListCustomMetrics" ]
    }
  }
}