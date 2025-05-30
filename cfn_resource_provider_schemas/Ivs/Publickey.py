SCHEMA = {
  "typeName" : "AWS::IVS::PublicKey",
  "description" : "Resource Type definition for AWS::IVS::PublicKey",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "Tag" : {
      "type" : "object",
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
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Name" : {
      "description" : "Name of the public key to be imported. The value does not need to be unique.",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9-_]*$",
      "minLength" : 0,
      "maxLength" : 128
    },
    "PublicKeyMaterial" : {
      "description" : "The public portion of a customer-generated key pair. This field is required to create the AWS::IVS::PublicKey resource.",
      "type" : "string",
      "pattern" : "-----BEGIN PUBLIC KEY-----\\r?\\n([a-zA-Z0-9+/=\\r\\n]+)\\r?\\n-----END PUBLIC KEY-----(\\r?\\n)?"
    },
    "Fingerprint" : {
      "description" : "Key-pair identifier.",
      "type" : "string"
    },
    "Arn" : {
      "description" : "Key-pair identifier.",
      "type" : "string",
      "pattern" : "^arn:aws:ivs:[a-z0-9-]+:[0-9]+:public-key/[a-zA-Z0-9-]+$",
      "minLength" : 1,
      "maxLength" : 128
    },
    "Tags" : {
      "description" : "A list of key-value pairs that contain metadata for the asset model.",
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
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "ivs:TagResource", "ivs:UntagResource", "ivs:ListTagsForResource" ]
  },
  "primaryIdentifier" : [ "/properties/Arn" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/Fingerprint" ],
  "createOnlyProperties" : [ "/properties/PublicKeyMaterial", "/properties/Name" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ivs:ImportPublicKey", "ivs:TagResource" ]
    },
    "read" : {
      "permissions" : [ "ivs:GetPublicKey" ]
    },
    "update" : {
      "permissions" : [ "ivs:GetPublicKey", "ivs:ListTagsForResource", "ivs:UntagResource", "ivs:TagResource" ]
    },
    "delete" : {
      "permissions" : [ "ivs:DeletePublicKey", "ivs:UntagResource" ]
    },
    "list" : {
      "permissions" : [ "ivs:ListPublicKeys", "ivs:ListTagsForResource" ]
    }
  }
}