SCHEMA = {
  "typeName" : "AWS::AppIntegrations::EventIntegration",
  "description" : "Resource Type definition for AWS::AppIntegrations::EventIntegration",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "EventFilter" : {
      "type" : "object",
      "properties" : {
        "Source" : {
          "description" : "The source of the events.",
          "type" : "string",
          "pattern" : "^aws\\.(partner\\/.*|cases)$",
          "minLength" : 1,
          "maxLength" : 256
        }
      },
      "additionalProperties" : False,
      "required" : [ "Source" ]
    },
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "description" : "A key to identify the tag.",
          "type" : "string",
          "pattern" : "^(?!aws:)[a-zA-Z+-=._:/]+$",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "description" : "Corresponding tag value for the key.",
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "additionalProperties" : False,
      "required" : [ "Key", "Value" ]
    },
    "Metadata" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "description" : "A key to identify the metadata.",
          "type" : "string",
          "pattern" : ".*\\S.*",
          "minLength" : 1,
          "maxLength" : 255
        },
        "Value" : {
          "description" : "Corresponding metadata value for the key.",
          "type" : "string",
          "pattern" : ".*\\S.*",
          "minLength" : 1,
          "maxLength" : 255
        }
      },
      "additionalProperties" : False,
      "required" : [ "Key", "Value" ]
    }
  },
  "properties" : {
    "Description" : {
      "description" : "The event integration description.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 1000
    },
    "EventIntegrationArn" : {
      "description" : "The Amazon Resource Name (ARN) of the event integration.",
      "type" : "string",
      "pattern" : "^arn:aws[-a-z]*:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$",
      "minLength" : 1,
      "maxLength" : 2048
    },
    "Name" : {
      "description" : "The name of the event integration.",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9/\\._\\-]+$",
      "minLength" : 1,
      "maxLength" : 255
    },
    "EventBridgeBus" : {
      "description" : "The Amazon Eventbridge bus for the event integration.",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9/\\._\\-]+$",
      "minLength" : 1,
      "maxLength" : 255
    },
    "EventFilter" : {
      "description" : "The EventFilter (source) associated with the event integration.",
      "$ref" : "#/definitions/EventFilter"
    },
    "Tags" : {
      "description" : "The tags (keys and values) associated with the event integration.",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "minItems" : 0,
      "maxItems" : 200
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "app-integrations:TagResource", "app-integrations:UntagResource" ]
  },
  "additionalProperties" : False,
  "required" : [ "Name", "EventBridgeBus", "EventFilter" ],
  "readOnlyProperties" : [ "/properties/EventIntegrationArn" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/EventBridgeBus", "/properties/EventFilter" ],
  "primaryIdentifier" : [ "/properties/Name" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "app-integrations:CreateEventIntegration", "app-integrations:TagResource" ]
    },
    "read" : {
      "permissions" : [ "app-integrations:GetEventIntegration", "app-integrations:ListTagsForResource" ]
    },
    "list" : {
      "permissions" : [ "app-integrations:ListEventIntegrations" ]
    },
    "update" : {
      "permissions" : [ "app-integrations:GetEventIntegration", "app-integrations:UpdateEventIntegration", "app-integrations:TagResource", "app-integrations:UntagResource" ]
    },
    "delete" : {
      "permissions" : [ "app-integrations:DeleteEventIntegration" ]
    }
  }
}