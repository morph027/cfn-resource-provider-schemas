SCHEMA = {
  "typeName" : "AWS::MediaPackageV2::ChannelGroup",
  "description" : "<p>Represents a channel group that facilitates the grouping of multiple channels.</p>",
  "properties" : {
    "Arn" : {
      "type" : "string",
      "description" : "<p>The Amazon Resource Name (ARN) associated with the resource.</p>"
    },
    "ChannelGroupName" : {
      "type" : "string",
      "maxLength" : 256,
      "minLength" : 1,
      "pattern" : "^[a-zA-Z0-9_-]+$"
    },
    "CreatedAt" : {
      "type" : "string",
      "description" : "<p>The date and time the channel group was created.</p>",
      "format" : "date-time"
    },
    "Description" : {
      "type" : "string",
      "maxLength" : 1024,
      "minLength" : 0,
      "description" : "<p>Enter any descriptive text that helps you to identify the channel group.</p>"
    },
    "EgressDomain" : {
      "type" : "string",
      "description" : "<p>The output domain where the source stream should be sent. Integrate the domain with a downstream CDN (such as Amazon CloudFront) or playback device.</p>"
    },
    "ModifiedAt" : {
      "type" : "string",
      "description" : "<p>The date and time the channel group was modified.</p>",
      "format" : "date-time"
    },
    "Tags" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "readOnlyProperties" : [ "/properties/Arn", "/properties/CreatedAt", "/properties/EgressDomain", "/properties/ModifiedAt" ],
  "createOnlyProperties" : [ "/properties/ChannelGroupName" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "mediapackagev2:TagResource", "mediapackagev2:CreateChannelGroup" ]
    },
    "read" : {
      "permissions" : [ "mediapackagev2:GetChannelGroup" ]
    },
    "update" : {
      "permissions" : [ "mediapackagev2:TagResource", "mediapackagev2:UntagResource", "mediapackagev2:ListTagsForResource", "mediapackagev2:UpdateChannelGroup" ]
    },
    "delete" : {
      "permissions" : [ "mediapackagev2:GetChannelGroup", "mediapackagev2:DeleteChannelGroup" ]
    },
    "list" : {
      "permissions" : [ "mediapackagev2:ListChannelGroups" ]
    }
  },
  "definitions" : {
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string"
        },
        "Value" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "mediapackagev2:TagResource", "mediapackagev2:UntagResource", "mediapackagev2:ListTagsForResource" ]
  },
  "required" : [ "ChannelGroupName" ],
  "additionalIdentifiers" : [ [ "/properties/ChannelGroupName" ] ],
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-mediapackagev2",
  "additionalProperties" : False
}