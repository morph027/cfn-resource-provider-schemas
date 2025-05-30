SCHEMA = {
  "typeName" : "AWS::Logs::DeliverySource",
  "description" : " A delivery source is an AWS resource that sends logs to an AWS destination. The destination can be CloudWatch Logs, Amazon S3, or Kinesis Data Firehose.\n\nOnly some AWS services support being configured as a delivery source. These services are listed as Supported [V2 Permissions] in the table at [Enabling logging from AWS services](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html).",
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
      "description" : "The Amazon Resource Name (ARN) that uniquely identifies this delivery source.",
      "type" : "string",
      "minLength" : 16,
      "maxLength" : 2048,
      "pattern" : "[\\w#+=/:,.@-]*\\*?"
    }
  },
  "properties" : {
    "Name" : {
      "description" : "The unique name of the Log source.",
      "type" : "string",
      "pattern" : "[\\w-]*$",
      "minLength" : 1,
      "maxLength" : 60
    },
    "Arn" : {
      "description" : "The Amazon Resource Name (ARN) that uniquely identifies this delivery source.",
      "$ref" : "#/definitions/Arn"
    },
    "ResourceArns" : {
      "description" : "This array contains the ARN of the AWS resource that sends logs and is represented by this delivery source. Currently, only one ARN can be in the array.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Arn"
      }
    },
    "ResourceArn" : {
      "description" : "The ARN of the resource that will be sending the logs.",
      "$ref" : "#/definitions/Arn"
    },
    "Service" : {
      "description" : "The AWS service that is sending logs.",
      "type" : "string",
      "pattern" : "[\\w-]*$",
      "minLength" : 1,
      "maxLength" : 255
    },
    "LogType" : {
      "description" : "The type of logs being delivered. Only mandatory when the resourceArn could match more than one. In such a case, the error message will contain all the possible options.",
      "type" : "string",
      "pattern" : "[\\w-]*$",
      "minLength" : 1,
      "maxLength" : 255
    },
    "Tags" : {
      "description" : "The tags that have been assigned to this delivery source.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "additionalProperties" : False,
  "required" : [ "Name" ],
  "createOnlyProperties" : [ "/properties/Name" ],
  "primaryIdentifier" : [ "/properties/Name" ],
  "writeOnlyProperties" : [ "/properties/ResourceArn" ],
  "readOnlyProperties" : [ "/properties/Service", "/properties/ResourceArns", "/properties/Arn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "logs:PutDeliverySource", "logs:GetDeliverySource", "logs:ListTagsForResource", "logs:TagResource", "logs:AllowVendedLogDeliveryForResource", "codewhisperer:AllowVendedLogDeliveryForResource", "autoloop:AllowVendedLogDeliveryForResource", "workmail:AllowVendedLogDeliveryForResource" ]
    },
    "read" : {
      "permissions" : [ "logs:GetDeliverySource", "logs:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "logs:PutDeliverySource", "logs:GetDeliverySource", "logs:ListTagsForResource", "logs:TagResource", "logs:UntagResource" ]
    },
    "delete" : {
      "permissions" : [ "logs:DeleteDeliverySource" ]
    },
    "list" : {
      "permissions" : [ "logs:DescribeDeliverySources" ]
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