SCHEMA = {
  "typeName" : "AWS::Bedrock::GuardrailVersion",
  "description" : "Definition of AWS::Bedrock::GuardrailVersion Resource Type",
  "definitions" : { },
  "properties" : {
    "Description" : {
      "type" : "string",
      "maxLength" : 200,
      "minLength" : 1,
      "description" : "Description of the Guardrail version"
    },
    "GuardrailArn" : {
      "type" : "string",
      "maxLength" : 2048,
      "pattern" : "^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:guardrail/[a-z0-9]+$",
      "description" : "Arn representation for the guardrail"
    },
    "GuardrailId" : {
      "type" : "string",
      "maxLength" : 64,
      "pattern" : "^[a-z0-9]+$",
      "description" : "Unique id for the guardrail"
    },
    "GuardrailIdentifier" : {
      "type" : "string",
      "maxLength" : 2048,
      "pattern" : "^(([a-z0-9]+)|(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:guardrail/[a-z0-9]+))$",
      "description" : "Identifier (GuardrailId or GuardrailArn) for the guardrail"
    },
    "Version" : {
      "type" : "string",
      "pattern" : "^[1-9][0-9]{0,7}$",
      "description" : "Guardrail version"
    }
  },
  "required" : [ "GuardrailIdentifier" ],
  "readOnlyProperties" : [ "/properties/GuardrailArn", "/properties/GuardrailId", "/properties/Version" ],
  "createOnlyProperties" : [ "/properties/Description", "/properties/GuardrailIdentifier" ],
  "writeOnlyProperties" : [ "/properties/GuardrailIdentifier" ],
  "primaryIdentifier" : [ "/properties/GuardrailId", "/properties/Version" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "bedrock:CreateGuardrailVersion", "bedrock:GetGuardrail", "kms:CreateGrant", "kms:Decrypt" ]
    },
    "read" : {
      "permissions" : [ "bedrock:GetGuardrail", "kms:Decrypt" ]
    },
    "delete" : {
      "permissions" : [ "bedrock:DeleteGuardrail", "bedrock:GetGuardrail", "kms:RetireGrant" ]
    }
  },
  "tagging" : {
    "taggable" : False
  },
  "additionalProperties" : False
}