SCHEMA = {
  "typeName" : "AWS::SecurityLake::SubscriberNotification",
  "description" : "Resource Type definition for AWS::SecurityLake::SubscriberNotification",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-securitylake.git",
  "definitions" : {
    "HttpsNotificationConfiguration" : {
      "type" : "object",
      "properties" : {
        "AuthorizationApiKeyName" : {
          "type" : "string",
          "description" : "The key name for the notification subscription."
        },
        "AuthorizationApiKeyValue" : {
          "type" : "string",
          "description" : "The key value for the notification subscription."
        },
        "Endpoint" : {
          "type" : "string",
          "pattern" : "^https?://.+$",
          "description" : "The subscription endpoint in Security Lake."
        },
        "HttpMethod" : {
          "type" : "string",
          "enum" : [ "POST", "PUT" ],
          "description" : "The HTTPS method used for the notification subscription."
        },
        "TargetRoleArn" : {
          "type" : "string",
          "pattern" : "^arn:.*$",
          "description" : "The Amazon Resource Name (ARN) of the EventBridge API destinations IAM role that you created."
        }
      },
      "description" : "The configuration for HTTPS subscriber notification.",
      "additionalProperties" : False,
      "required" : [ "Endpoint", "TargetRoleArn" ]
    },
    "SqsNotificationConfiguration" : {
      "type" : "object",
      "description" : "The configurations for SQS subscriber notification. The members of this structure are context-dependent."
    },
    "NotificationConfiguration" : {
      "type" : "object",
      "properties" : {
        "HttpsNotificationConfiguration" : {
          "$ref" : "#/definitions/HttpsNotificationConfiguration"
        },
        "SqsNotificationConfiguration" : {
          "$ref" : "#/definitions/SqsNotificationConfiguration"
        }
      },
      "additionalProperties" : False,
      "oneOf" : [ {
        "required" : [ "HttpsNotificationConfiguration" ]
      }, {
        "required" : [ "SqsNotificationConfiguration" ]
      } ]
    }
  },
  "properties" : {
    "NotificationConfiguration" : {
      "$ref" : "#/definitions/NotificationConfiguration"
    },
    "SubscriberArn" : {
      "description" : "The ARN for the subscriber",
      "type" : "string",
      "pattern" : "^arn:.*$"
    },
    "SubscriberEndpoint" : {
      "description" : "The endpoint the subscriber should listen to for notifications",
      "type" : "string"
    }
  },
  "tagging" : {
    "taggable" : False
  },
  "additionalProperties" : False,
  "required" : [ "SubscriberArn", "NotificationConfiguration" ],
  "primaryIdentifier" : [ "/properties/SubscriberArn" ],
  "readOnlyProperties" : [ "/properties/SubscriberEndpoint" ],
  "createOnlyProperties" : [ "/properties/SubscriberArn" ],
  "writeOnlyProperties" : [ "/properties/NotificationConfiguration/HttpsNotificationConfiguration/AuthorizationApiKeyName", "/properties/NotificationConfiguration/HttpsNotificationConfiguration/AuthorizationApiKeyValue", "/properties/NotificationConfiguration/HttpsNotificationConfiguration/Endpoint", "/properties/NotificationConfiguration/HttpsNotificationConfiguration/HttpMethod", "/properties/NotificationConfiguration/HttpsNotificationConfiguration/TargetRoleArn" ],
  "replacementStrategy" : "delete_then_create",
  "handlers" : {
    "create" : {
      "permissions" : [ "securitylake:CreateDataLake", "securitylake:CreateSubscriber", "securitylake:CreateSubscriberNotification", "securitylake:GetSubscriber", "iam:CreateServiceLinkedRole", "iam:PutRolePolicy", "iam:DeleteRolePolicy", "iam:PassRole", "s3:PutBucketNotification", "s3:GetBucketNotification", "events:CreateApiDestination", "events:CreateConnection", "events:CreateRule", "events:UpdateConnection", "events:DeleteConnection", "events:UpdateApiDestination", "events:DeleteApiDestination", "events:ListApiDestinations", "events:ListConnections", "events:PutRule", "events:DescribeRule", "events:DeleteRule", "events:PutTargets", "events:RemoveTargets", "events:ListTargetsByRule", "secretsmanager:CreateSecret", "sqs:CreateQueue", "sqs:GetQueueAttributes", "sqs:GetQueueUrl", "sqs:SetQueueAttributes" ]
    },
    "read" : {
      "permissions" : [ "securitylake:GetSubscriber" ]
    },
    "update" : {
      "permissions" : [ "securitylake:UpdateSubscriberNotification", "securitylake:GetSubscriber", "iam:CreateServiceLinkedRole", "iam:PutRolePolicy", "iam:DeleteRolePolicy", "iam:PassRole", "events:CreateApiDestination", "events:CreateConnection", "events:UpdateConnection", "events:DeleteConnection", "events:UpdateApiDestination", "events:DeleteApiDestination", "events:DeleteRule", "events:ListApiDestinations", "events:ListConnections", "events:PutRule", "events:DescribeRule", "events:DeleteRule", "events:PutTargets", "events:RemoveTargets", "events:ListTargetsByRule", "secretsmanager:CreateSecret", "s3:GetBucketNotificationConfiguration", "s3:PutBucketNotificationConfiguration", "s3:PutBucketNotification", "s3:GetBucketNotification", "sqs:CreateQueue", "sqs:DeleteQueue", "sqs:GetQueueAttributes", "sqs:SetQueueAttributes" ]
    },
    "delete" : {
      "permissions" : [ "securitylake:DeleteSubscriberNotification", "securitylake:GetSubscriber", "iam:DeleteRole", "iam:DeleteRolePolicy", "events:DeleteApiDestination", "events:DeleteConnection", "events:DeleteRule", "events:ListTargetsByRule", "events:DescribeRule", "events:RemoveTargets", "sqs:DeleteQueue" ]
    },
    "list" : {
      "permissions" : [ "securitylake:ListSubscribers" ]
    }
  }
}