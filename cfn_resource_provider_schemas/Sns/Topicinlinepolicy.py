SCHEMA = {
  "typeName" : "AWS::SNS::TopicInlinePolicy",
  "description" : "Schema for AWS::SNS::TopicInlinePolicy",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-sns.git",
  "additionalProperties" : False,
  "properties" : {
    "PolicyDocument" : {
      "description" : "A policy document that contains permissions to add to the specified SNS topics.",
      "type" : "object"
    },
    "TopicArn" : {
      "description" : "The Amazon Resource Name (ARN) of the topic to which you want to add the policy.",
      "type" : "string"
    }
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "required" : [ "PolicyDocument", "TopicArn" ],
  "primaryIdentifier" : [ "/properties/TopicArn" ],
  "createOnlyProperties" : [ "/properties/TopicArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "sns:SetTopicAttributes", "sns:GetTopicAttributes" ]
    },
    "read" : {
      "permissions" : [ "sns:GetTopicAttributes" ]
    },
    "delete" : {
      "permissions" : [ "sns:SetTopicAttributes", "sns:GetTopicAttributes" ]
    },
    "update" : {
      "permissions" : [ "sns:SetTopicAttributes", "sns:GetTopicAttributes" ]
    }
  }
}