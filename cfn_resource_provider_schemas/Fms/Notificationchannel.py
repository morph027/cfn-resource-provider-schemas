SCHEMA = {
  "typeName" : "AWS::FMS::NotificationChannel",
  "description" : "Designates the IAM role and Amazon Simple Notification Service (SNS) topic that AWS Firewall Manager uses to record SNS logs.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-fms.git",
  "definitions" : {
    "ResourceArn" : {
      "description" : "A resource ARN.",
      "type" : "string",
      "pattern" : "^([^\\s]+)$",
      "minLength" : 1,
      "maxLength" : 1024
    }
  },
  "properties" : {
    "SnsRoleName" : {
      "$ref" : "#/definitions/ResourceArn"
    },
    "SnsTopicArn" : {
      "$ref" : "#/definitions/ResourceArn"
    }
  },
  "required" : [ "SnsRoleName", "SnsTopicArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "fms:PutNotificationChannel", "iam:PassRole" ]
    },
    "update" : {
      "permissions" : [ "fms:PutNotificationChannel", "iam:PassRole" ]
    },
    "read" : {
      "permissions" : [ "fms:GetNotificationChannel" ]
    },
    "delete" : {
      "permissions" : [ "fms:DeleteNotificationChannel" ]
    },
    "list" : {
      "permissions" : [ "fms:GetNotificationChannel" ]
    }
  },
  "primaryIdentifier" : [ "/properties/SnsTopicArn" ],
  "additionalProperties" : False
}