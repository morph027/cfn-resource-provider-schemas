SCHEMA = {
  "typeName" : "AWS::SES::ConfigurationSetEventDestination",
  "description" : "Resource Type definition for AWS::SES::ConfigurationSetEventDestination",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-ses.git",
  "definitions" : {
    "EventDestination" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Name" : {
          "description" : "The name of the event destination set.",
          "type" : "string",
          "pattern" : "^[a-zA-Z0-9_-]{0,64}$"
        },
        "Enabled" : {
          "description" : "Sets whether Amazon SES publishes events to this destination when you send an email with the associated configuration set. Set to True to enable publishing to this destination; set to False to prevent publishing to this destination. The default value is false.   ",
          "type" : "boolean"
        },
        "MatchingEventTypes" : {
          "type" : "array",
          "uniqueItems" : False,
          "insertionOrder" : False,
          "description" : "The type of email sending events, send, reject, bounce, complaint, delivery, open, click, renderingFailure, deliveryDelay, and subscription.",
          "items" : {
            "type" : "string"
          }
        },
        "CloudWatchDestination" : {
          "description" : "An object that contains the names, default values, and sources of the dimensions associated with an Amazon CloudWatch event destination.",
          "$ref" : "#/definitions/CloudWatchDestination"
        },
        "KinesisFirehoseDestination" : {
          "description" : "An object that contains the delivery stream ARN and the IAM role ARN associated with an Amazon Kinesis Firehose event destination.",
          "$ref" : "#/definitions/KinesisFirehoseDestination"
        },
        "SnsDestination" : {
          "description" : "An object that contains SNS topic ARN associated event destination.",
          "$ref" : "#/definitions/SnsDestination"
        },
        "EventBridgeDestination" : {
          "description" : "An object that contains Event bus ARN associated with the event bridge destination.",
          "$ref" : "#/definitions/EventBridgeDestination"
        }
      },
      "required" : [ "MatchingEventTypes" ]
    },
    "EventBridgeDestination" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "An object that contains Event bus ARN associated with the event bridge destination.",
      "properties" : {
        "EventBusArn" : {
          "type" : "string",
          "minLength" : 36,
          "maxLength" : 1024,
          "pattern" : "^arn:aws[a-z0-9-]*:events:[a-z0-9-]+:\\d{12}:event-bus/[^:]+$"
        }
      },
      "required" : [ "EventBusArn" ]
    },
    "SnsDestination" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "An object that contains SNS topic ARN associated event destination.",
      "properties" : {
        "TopicARN" : {
          "type" : "string",
          "minLength" : 36,
          "maxLength" : 1024,
          "pattern" : "^arn:aws[a-z0-9-]*:sns:[a-z0-9-]+:\\d{12}:[^:]+$"
        }
      },
      "required" : [ "TopicARN" ]
    },
    "KinesisFirehoseDestination" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "An object that contains the delivery stream ARN and the IAM role ARN associated with an Amazon Kinesis Firehose event destination.",
      "properties" : {
        "IAMRoleARN" : {
          "description" : "The ARN of the IAM role under which Amazon SES publishes email sending events to the Amazon Kinesis Firehose stream.",
          "type" : "string"
        },
        "DeliveryStreamARN" : {
          "description" : "The ARN of the Amazon Kinesis Firehose stream that email sending events should be published to.",
          "type" : "string"
        }
      },
      "required" : [ "IAMRoleARN", "DeliveryStreamARN" ]
    },
    "CloudWatchDestination" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "An object that contains the names, default values, and sources of the dimensions associated with an Amazon CloudWatch event destination.",
      "properties" : {
        "DimensionConfigurations" : {
          "type" : "array",
          "uniqueItems" : False,
          "insertionOrder" : False,
          "description" : "A list of dimensions upon which to categorize your emails when you publish email sending events to Amazon CloudWatch.",
          "items" : {
            "$ref" : "#/definitions/DimensionConfiguration"
          }
        }
      }
    },
    "DimensionConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "A list of dimensions upon which to categorize your emails when you publish email sending events to Amazon CloudWatch.",
      "properties" : {
        "DimensionValueSource" : {
          "description" : "The place where Amazon SES finds the value of a dimension to publish to Amazon CloudWatch. To use the message tags that you specify using an X-SES-MESSAGE-TAGS header or a parameter to the SendEmail/SendRawEmail API, specify messageTag. To use your own email headers, specify emailHeader. To put a custom tag on any link included in your email, specify linkTag.",
          "type" : "string"
        },
        "DefaultDimensionValue" : {
          "description" : "The default value of the dimension that is published to Amazon CloudWatch if you do not provide the value of the dimension when you send an email.",
          "type" : "string",
          "pattern" : "^[a-zA-Z0-9_-]{1,256}$",
          "maxLength" : 256,
          "minLength" : 1
        },
        "DimensionName" : {
          "description" : "The name of an Amazon CloudWatch dimension associated with an email sending metric.",
          "type" : "string",
          "pattern" : "^[a-zA-Z0-9_:-]{1,256}$",
          "maxLength" : 256,
          "minLength" : 1
        }
      },
      "required" : [ "DimensionValueSource", "DefaultDimensionValue", "DimensionName" ]
    }
  },
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "ConfigurationSetName" : {
      "description" : "The name of the configuration set that contains the event destination.",
      "type" : "string"
    },
    "EventDestination" : {
      "description" : "The event destination object.",
      "$ref" : "#/definitions/EventDestination"
    }
  },
  "additionalProperties" : False,
  "taggable" : False,
  "required" : [ "ConfigurationSetName", "EventDestination" ],
  "createOnlyProperties" : [ "/properties/ConfigurationSetName" ],
  "readOnlyProperties" : [ "/properties/Id" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ses:CreateConfigurationSetEventDestination", "ses:GetConfigurationSetEventDestinations", "ses:DescribeConfigurationSet" ]
    },
    "update" : {
      "permissions" : [ "ses:UpdateConfigurationSetEventDestination", "ses:GetConfigurationSetEventDestinations" ]
    },
    "delete" : {
      "permissions" : [ "ses:DeleteConfigurationSetEventDestination" ]
    },
    "read" : {
      "permissions" : [ "ses:GetConfigurationSetEventDestinations", "ses:DescribeConfigurationSet" ]
    }
  }
}