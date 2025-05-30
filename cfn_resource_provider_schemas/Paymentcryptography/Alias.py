SCHEMA = {
  "typeName" : "AWS::PaymentCryptography::Alias",
  "description" : "Definition of AWS::PaymentCryptography::Alias Resource Type",
  "properties" : {
    "AliasName" : {
      "type" : "string",
      "maxLength" : 256,
      "minLength" : 7,
      "pattern" : "^alias/[a-zA-Z0-9/_-]+$"
    },
    "KeyArn" : {
      "type" : "string",
      "maxLength" : 150,
      "minLength" : 70,
      "pattern" : "^arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:key/[0-9a-zA-Z]{16,64}$"
    }
  },
  "createOnlyProperties" : [ "/properties/AliasName" ],
  "primaryIdentifier" : [ "/properties/AliasName" ],
  "required" : [ "AliasName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "payment-cryptography:CreateAlias" ]
    },
    "read" : {
      "permissions" : [ "payment-cryptography:GetAlias" ]
    },
    "update" : {
      "permissions" : [ "payment-cryptography:UpdateAlias" ]
    },
    "delete" : {
      "permissions" : [ "payment-cryptography:DeleteAlias" ]
    },
    "list" : {
      "permissions" : [ "payment-cryptography:ListAliases" ]
    }
  },
  "tagging" : {
    "taggable" : False
  },
  "additionalProperties" : False
}