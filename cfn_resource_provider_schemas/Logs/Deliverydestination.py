SCHEMA = {
  "typeName" : "AWS::Logs::DeliveryDestination",
  "description" : "This structure contains information about one delivery destination in your account.\n\nA delivery destination is an AWS resource that represents an AWS service that logs can be sent to CloudWatch Logs, Amazon S3, are supported as Kinesis Data Firehose delivery destinations.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-logs.git",
  "definitions" : {
    "Arn" : {
      "description" : "The Amazon Resource Name (ARN) that uniquely identifies a resource.",
      "type" : "string",
      "minLength" : 16,
      "maxLength" : 2048,
      "pattern" : "[\\w#+=/:,.@-]*\\*?"
    },
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
    "DestinationPolicy" : {
      "type" : "object",
      "properties" : {
        "DeliveryDestinationName" : {
          "type" : "string",
          "description" : "The name of the delivery destination to assign this policy to",
          "minLength" : 1,
          "maxLength" : 60
        },
        "DeliveryDestinationPolicy" : {
          "type" : "object",
          "description" : "The contents of the policy attached to the delivery destination"
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Name" : {
      "description" : "The name of this delivery destination.",
      "type" : "string",
      "pattern" : "[\\w-]*$",
      "minLength" : 1,
      "maxLength" : 60
    },
    "Arn" : {
      "description" : "The Amazon Resource Name (ARN) that uniquely identifies this delivery destination.",
      "$ref" : "#/definitions/Arn"
    },
    "DestinationResourceArn" : {
      "description" : "The ARN of the Amazon Web Services destination that this delivery destination represents. That Amazon Web Services destination can be a log group in CloudWatch Logs, an Amazon S3 bucket, or a delivery stream in Firehose.",
      "$ref" : "#/definitions/Arn"
    },
    "Tags" : {
      "description" : "The tags that have been assigned to this delivery destination.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "DeliveryDestinationType" : {
      "description" : "Displays whether this delivery destination is CloudWatch Logs, Amazon S3, or Kinesis Data Firehose.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 12,
      "pattern" : "^[0-9A-Za-z]+$"
    },
    "DeliveryDestinationPolicy" : {
      "description" : "IAM policy that grants permissions to CloudWatch Logs to deliver logs cross-account to a specified destination in this account.\n\nThe policy must be in JSON string format.\n\nLength Constraints: Maximum length of 51200",
      "type" : "object",
      "$ref" : "#/definitions/DestinationPolicy"
    },
    "OutputFormat" : {
      "description" : "The format of the logs that are sent to this delivery destination.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 12,
      "pattern" : "^[0-9A-Za-z]+$"
    }
  },
  "additionalProperties" : False,
  "required" : [ "Name" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/OutputFormat", "/properties/DestinationResourceArn" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/DeliveryDestinationType" ],
  "primaryIdentifier" : [ "/properties/Name" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "logs:PutDeliveryDestination", "logs:GetDeliveryDestination", "logs:ListTagsForResource", "logs:TagResource", "logs:UntagResource", "logs:PutDeliveryDestinationPolicy", "logs:GetDeliveryDestinationPolicy" ]
    },
    "read" : {
      "permissions" : [ "logs:GetDeliveryDestination", "logs:ListTagsForResource", "logs:GetDeliveryDestinationPolicy" ]
    },
    "update" : {
      "permissions" : [ "logs:PutDeliveryDestination", "logs:GetDeliveryDestination", "logs:ListTagsForResource", "logs:TagResource", "logs:UntagResource", "logs:DeleteDeliveryDestinationPolicy", "logs:PutDeliveryDestinationPolicy", "logs:GetDeliveryDestinationPolicy" ]
    },
    "delete" : {
      "permissions" : [ "logs:DeleteDeliveryDestination", "logs:DeleteDeliveryDestinationPolicy" ]
    },
    "list" : {
      "permissions" : [ "logs:DescribeDeliveryDestinations", "logs:GetDeliveryDestinationPolicy" ]
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