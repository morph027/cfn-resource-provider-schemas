SCHEMA = {
  "typeName" : "AWS::SQS::QueueInlinePolicy",
  "description" : "Schema for SQS QueueInlinePolicy",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-sqs.git",
  "properties" : {
    "PolicyDocument" : {
      "description" : "A policy document that contains permissions to add to the specified SQS queue",
      "type" : "object"
    },
    "Queue" : {
      "description" : "The URL of the SQS queue.",
      "type" : "string"
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "required" : [ "PolicyDocument", "Queue" ],
  "primaryIdentifier" : [ "/properties/Queue" ],
  "createOnlyProperties" : [ "/properties/Queue" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "sqs:SetQueueAttributes", "sqs:GetQueueAttributes", "sqs:GetQueueUrl" ]
    },
    "read" : {
      "permissions" : [ "sqs:GetQueueAttributes", "sqs:GetQueueUrl" ]
    },
    "delete" : {
      "permissions" : [ "sqs:SetQueueAttributes", "sqs:GetQueueAttributes" ]
    },
    "update" : {
      "permissions" : [ "sqs:SetQueueAttributes", "sqs:GetQueueAttributes", "sqs:GetQueueUrl" ]
    }
  }
}