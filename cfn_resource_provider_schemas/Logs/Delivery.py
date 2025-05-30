SCHEMA = {
  "typeName" : "AWS::Logs::Delivery",
  "description" : "This structure contains information about one delivery in your account.\n\nA delivery is a connection between a logical delivery source and a logical delivery destination.\n\nFor more information, see [CreateDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html).",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-logs.git",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    },
    "Arn" : {
      "description" : "Amazon Resource Name (ARN) that uniquely identify AWS resource.",
      "type" : "string",
      "minLength" : 16,
      "maxLength" : 2048,
      "pattern" : "[\\w#+=/:,.@-]*\\*?"
    },
    "FieldHeader" : {
      "description" : "A single record field to be delivered to the destination.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 50
    }
  },
  "properties" : {
    "DeliveryId" : {
      "description" : "The unique ID that identifies this delivery in your account.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 64,
      "pattern" : "^[0-9A-Za-z]+$"
    },
    "Arn" : {
      "description" : "The Amazon Resource Name (ARN) that uniquely identifies this delivery.",
      "$ref" : "#/definitions/Arn"
    },
    "DeliverySourceName" : {
      "description" : "The name of the delivery source that is associated with this delivery.",
      "type" : "string",
      "pattern" : "[\\w-]*$",
      "minLength" : 1,
      "maxLength" : 60
    },
    "DeliveryDestinationArn" : {
      "description" : "The ARN of the delivery destination that is associated with this delivery.",
      "$ref" : "#/definitions/Arn"
    },
    "DeliveryDestinationType" : {
      "description" : "Displays whether the delivery destination associated with this delivery is CloudWatch Logs, Amazon S3, or Kinesis Data Firehose.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 12,
      "pattern" : "^[0-9A-Za-z]+$"
    },
    "Tags" : {
      "description" : "The tags that have been assigned to this delivery.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "RecordFields" : {
      "description" : "The list of record fields to be delivered to the destination, in order. If the delivery's log source has mandatory fields, they must be included in this list.",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/FieldHeader"
      }
    },
    "FieldDelimiter" : {
      "description" : "The field delimiter to use between record fields when the final output format of a delivery is in Plain , W3C , or Raw format.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 5
    },
    "S3SuffixPath" : {
      "description" : "This string allows re-configuring the S3 object prefix to contain either static or variable sections. The valid variables to use in the suffix path will vary by each log source. See ConfigurationTemplate$allowedSuffixPathFields for more info on what values are supported in the suffix path for each log source.",
      "type" : "string",
      "minLength" : 0,
      "maxLength" : 256
    },
    "S3EnableHiveCompatiblePath" : {
      "description" : "This parameter causes the S3 objects that contain delivered logs to use a prefix structure that allows for integration with Apache Hive.",
      "type" : "boolean"
    }
  },
  "additionalProperties" : False,
  "required" : [ "DeliverySourceName", "DeliveryDestinationArn" ],
  "readOnlyProperties" : [ "/properties/DeliveryId", "/properties/Arn", "/properties/DeliveryDestinationType" ],
  "createOnlyProperties" : [ "/properties/DeliverySourceName", "/properties/DeliveryDestinationArn" ],
  "primaryIdentifier" : [ "/properties/DeliveryId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "logs:CreateDelivery", "logs:GetDelivery", "logs:DescribeDeliveries", "logs:ListTagsForResource", "logs:TagResource", "logs:GetDeliverySource", "logs:GetDeliveryDestination" ]
    },
    "read" : {
      "permissions" : [ "logs:GetDelivery", "logs:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "logs:GetDelivery", "logs:ListTagsForResource", "logs:TagResource", "logs:UntagResource", "logs:UpdateDeliveryConfiguration" ]
    },
    "delete" : {
      "permissions" : [ "logs:DeleteDelivery", "logs:ListTagsForResource", "logs:UntagResource" ]
    },
    "list" : {
      "permissions" : [ "logs:DescribeDeliveries", "logs:ListTagsForResource" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "logs:TagResource", "logs:UntagResource", "logs:ListTagsForResource" ]
  }
}