SCHEMA = {
  "typeName" : "AWS::Logs::Destination",
  "description" : "The AWS::Logs::Destination resource specifies a CloudWatch Logs destination. A destination encapsulates a physical resource (such as an Amazon Kinesis data stream) and enables you to subscribe that resource to a stream of log events.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-logs.git",
  "tagging" : {
    "taggable" : False
  },
  "properties" : {
    "Arn" : {
      "type" : "string"
    },
    "DestinationName" : {
      "description" : "The name of the destination resource",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 512,
      "pattern" : "^[^:*]{1,512}$"
    },
    "DestinationPolicy" : {
      "description" : "An IAM policy document that governs which AWS accounts can create subscription filters against this destination.",
      "type" : "string",
      "minLength" : 1
    },
    "RoleArn" : {
      "description" : "The ARN of an IAM role that permits CloudWatch Logs to send data to the specified AWS resource",
      "type" : "string",
      "minLength" : 1
    },
    "TargetArn" : {
      "description" : "The ARN of the physical target where the log events are delivered (for example, a Kinesis stream)",
      "type" : "string",
      "minLength" : 1
    }
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "logs:PutDestination", "logs:PutDestinationPolicy", "logs:DescribeDestinations", "iam:PassRole" ]
    },
    "read" : {
      "permissions" : [ "logs:DescribeDestinations" ]
    },
    "update" : {
      "permissions" : [ "logs:PutDestination", "logs:PutDestinationPolicy", "logs:DescribeDestinations", "iam:PassRole" ]
    },
    "delete" : {
      "permissions" : [ "logs:DeleteDestination" ]
    },
    "list" : {
      "permissions" : [ "logs:DescribeDestinations" ]
    }
  },
  "required" : [ "DestinationName", "TargetArn", "RoleArn" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/DestinationName" ],
  "primaryIdentifier" : [ "/properties/DestinationName" ],
  "additionalProperties" : False
}