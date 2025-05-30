SCHEMA = {
  "typeName" : "AWS::IVS::EncoderConfiguration",
  "description" : "Resource Type definition for AWS::IVS::EncoderConfiguration.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Arn" : {
      "description" : "Encoder configuration identifier.",
      "type" : "string",
      "pattern" : "^arn:aws:ivs:[a-z0-9-]+:[0-9]+:encoder-configuration/[a-zA-Z0-9-]+$",
      "minLength" : 1,
      "maxLength" : 128
    },
    "Video" : {
      "description" : "Video configuration. Default: video resolution 1280x720, bitrate 2500 kbps, 30 fps",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Bitrate" : {
          "description" : "Bitrate for generated output, in bps. Default: 2500000.",
          "type" : "integer",
          "minimum" : 1,
          "maximum" : 8500000,
          "default" : 2500000
        },
        "Framerate" : {
          "description" : "Video frame rate, in fps. Default: 30.",
          "type" : "number",
          "minimum" : 1,
          "maximum" : 60,
          "default" : 30
        },
        "Height" : {
          "description" : "Video-resolution height. This must be an even number. Note that the maximum value is determined by width times height, such that the maximum total pixels is 2073600 (1920x1080 or 1080x1920). Default: 720.",
          "type" : "integer",
          "minimum" : 2,
          "maximum" : 1920,
          "default" : 720
        },
        "Width" : {
          "description" : "Video-resolution width. This must be an even number. Note that the maximum value is determined by width times height, such that the maximum total pixels is 2073600 (1920x1080 or 1080x1920). Default: 1280.",
          "type" : "integer",
          "minimum" : 2,
          "maximum" : 1920,
          "default" : 1280
        }
      }
    },
    "Name" : {
      "description" : "Encoder configuration name.",
      "type" : "string",
      "maxLength" : 128,
      "minLength" : 0,
      "pattern" : "^[a-zA-Z0-9-_]*$"
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this resource.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "maxItems" : 50,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "additionalProperties" : False,
  "required" : [ ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "ivs:TagResource", "ivs:UntagResource", "ivs:ListTagsForResource" ]
  },
  "readOnlyProperties" : [ "/properties/Arn" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/Video", "/properties/Video/Bitrate", "/properties/Video/Framerate", "/properties/Video/Height", "/properties/Video/Width" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ivs:CreateEncoderConfiguration", "ivs:TagResource" ]
    },
    "read" : {
      "permissions" : [ "ivs:GetEncoderConfiguration", "ivs:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "ivs:GetEncoderConfiguration", "ivs:ListTagsForResource", "ivs:UntagResource", "ivs:TagResource" ]
    },
    "delete" : {
      "permissions" : [ "ivs:DeleteEncoderConfiguration", "ivs:UntagResource" ]
    },
    "list" : {
      "permissions" : [ "ivs:ListEncoderConfigurations", "ivs:ListTagsForResource" ]
    }
  }
}