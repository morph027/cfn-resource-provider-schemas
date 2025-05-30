SCHEMA = {
  "typeName" : "AWS::SNS::TopicPolicy",
  "description" : "The ``AWS::SNS::TopicPolicy`` resource associates SNS topics with a policy. For an example snippet, see [Declaring an policy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-iam.html#scenario-sns-policy) in the *User Guide*.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-sns.git",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "description" : "",
      "type" : "string"
    },
    "PolicyDocument" : {
      "description" : "A policy document that contains permissions to add to the specified SNS topics.",
      "type" : [ "object", "string" ]
    },
    "Topics" : {
      "description" : "The Amazon Resource Names (ARN) of the topics to which you want to add the policy. You can use the ``Ref`` function to specify an ``AWS::SNS::Topic`` resource.",
      "type" : "array",
      "uniqueItems" : False,
      "insertionOrder" : False,
      "items" : {
        "type" : "string"
      }
    }
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "required" : [ "PolicyDocument", "Topics" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "sns:SetTopicAttributes" ]
    },
    "update" : {
      "permissions" : [ "sns:SetTopicAttributes" ]
    },
    "delete" : {
      "permissions" : [ "sns:SetTopicAttributes" ]
    }
  }
}