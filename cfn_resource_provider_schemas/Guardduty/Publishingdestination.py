SCHEMA = {
  "typeName" : "AWS::GuardDuty::PublishingDestination",
  "description" : "Resource Type definition for AWS::GuardDuty::PublishingDestination.",
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "guardduty:TagResource", "guardduty:UntagResource", "guardduty:ListTagsForResource" ]
  },
  "properties" : {
    "Id" : {
      "type" : "string",
      "description" : "The ID of the publishing destination."
    },
    "DetectorId" : {
      "type" : "string",
      "description" : "The ID of the GuardDuty detector associated with the publishing destination.",
      "minLength" : 1,
      "maxLength" : 300
    },
    "DestinationType" : {
      "type" : "string",
      "description" : "The type of resource for the publishing destination. Currently only Amazon S3 buckets are supported."
    },
    "DestinationProperties" : {
      "type" : "object",
      "$ref" : "#/definitions/CFNDestinationProperties"
    },
    "Status" : {
      "type" : "string",
      "description" : "The status of the publishing destination."
    },
    "PublishingFailureStartTimestamp" : {
      "type" : "string",
      "description" : "The time, in epoch millisecond format, at which GuardDuty was first unable to publish findings to the destination."
    },
    "Tags" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/TagItem"
      }
    }
  },
  "definitions" : {
    "TagItem" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ]
    },
    "CFNDestinationProperties" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "DestinationArn" : {
          "type" : "string",
          "description" : "The ARN of the resource to publish to."
        },
        "KmsKeyArn" : {
          "type" : "string",
          "description" : "The ARN of the KMS key to use for encryption."
        }
      }
    }
  },
  "required" : [ "DetectorId", "DestinationType", "DestinationProperties" ],
  "primaryIdentifier" : [ "/properties/DetectorId", "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id", "/properties/Status", "/properties/PublishingFailureStartTimestamp" ],
  "createOnlyProperties" : [ "/properties/DetectorId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "guardduty:CreatePublishingDestination", "guardduty:TagResource", "guardduty:DescribePublishingDestination", "guardduty:ListTagsForResource" ]
    },
    "read" : {
      "permissions" : [ "guardduty:DescribePublishingDestination", "guardduty:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "guardduty:UpdatePublishingDestination", "guardduty:TagResource", "guardduty:UntagResource", "guardduty:ListTagsForResource", "guardduty:DescribePublishingDestination" ]
    },
    "delete" : {
      "permissions" : [ "guardduty:DeletePublishingDestination", "guardduty:DescribePublishingDestination" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "DetectorId" : {
            "type" : "string"
          }
        }
      },
      "permissions" : [ "guardduty:ListPublishingDestinations" ]
    }
  }
}